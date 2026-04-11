import re
import json
import sys


def parse_type(type_str: str):
    """Parse a TL type string into components."""
    is_vector = False
    inner = type_str.strip()

    # Vector<X> or vector<X>
    vec_match = re.match(r'^[Vv]ector\s*<(.+)>$', inner)
    if vec_match:
        is_vector = True
        inner = vec_match.group(1).strip()

    return inner, is_vector


def parse_field(token: str, flag_groups: dict):
    """
    Parse a single field token like:
      name:type
      name:flags.N?type
      name:flags2.N?type
      flags:#   (flag indicator)
    """
    colon = token.index(':')
    name = token[:colon]
    type_raw = token[colon + 1:]

    # Flag indicator: flags:# or flags2:#
    if type_raw == '#':
        group_num = flag_groups.get(name, len(flag_groups))
        flag_groups[name] = group_num
        return {
            "name": name,
            "type": "int",
            "flag_group": group_num,
            "flag_indicator": True,
        }

    # Optional field: flags.N?type  or  flags2.N?type
    opt_match = re.match(r'^(flags\d*)\s*\.\s*(\d+)\s*\?(.+)$', type_raw)
    if opt_match:
        flag_var = opt_match.group(1)   # e.g. "flags" or "flags2"
        flag_bit = int(opt_match.group(2))
        inner_type = opt_match.group(3).strip()
        group_num = flag_groups.get(flag_var, 0)

        inner_type, is_vector = parse_type(inner_type)

        field = {
            "name": name,
            "type": inner_type,
            "flag_group": group_num,
            "flag_bit": flag_bit,
        }
        if is_vector:
            field["is_vector"] = True
        return field

    # Plain field
    inner_type, is_vector = parse_type(type_raw)
    field = {
        "name": name,
        "type": inner_type,
    }
    if is_vector:
        field["is_vector"] = True
    return field


def parse_tl_line(line: str):
    """
    Parse one TL constructor line, e.g.:
      channel#8e87ccd8 flags:# ... = Chat;
    Returns a dict with constructor, id, return_type, fields.
    """
    line = line.strip().rstrip(';')
    if not line or line.startswith('//'):
        return None

    eq_idx = line.rfind('=')
    if eq_idx == -1:
        return None

    return_type = line[eq_idx + 1:].strip()
    left = line[:eq_idx].strip()

    tokens = left.split()
    if not tokens:
        return None

    # name#hexid
    name_hex = tokens[0]
    hash_idx = name_hex.find('#')
    if hash_idx != -1:
        name = name_hex[:hash_idx]
        cid_hex = name_hex[hash_idx + 1:]
        cid = int(cid_hex, 16)
    else:
        name = name_hex
        cid = 0

    # Track flag groups: { "flags": 0, "flags2": 1, ... }
    flag_groups: dict = {}

    # Pre-scan for flag indicators to register their group numbers
    for tok in tokens[1:]:
        if ':' in tok:
            colon = tok.index(':')
            fname = tok[:colon]
            ftype = tok[colon + 1:]
            if ftype == '#':
                if fname not in flag_groups:
                    flag_groups[fname] = len(flag_groups)

    fields = []
    for tok in tokens[1:]:
        # Skip generic type params like {t:Type}
        if tok.startswith('{') or tok in ('#', '[', ']'):
            continue
        if ':' not in tok:
            continue
        try:
            field = parse_field(tok, flag_groups)
            fields.append(field)
        except Exception:
            continue

    return {
        "constructor": name,
        "id": f"0x{cid:08x}",
        "return_type": return_type,
        "fields": fields,
    }


def parse_tl_file(path: str) -> dict:
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()

    constructors = []
    for line in lines:
        parsed = parse_tl_line(line)
        if parsed:
            constructors.append(parsed)

    # Group by return_type for convenience
    grouped: dict = {}
    for c in constructors:
        rt = c["return_type"]
        grouped.setdefault(rt, []).append(c["constructor"])

    return {
        "constructors": constructors,
        "grouped_by_type": grouped,
    }


def main():
    input_file  = sys.argv[1] if len(sys.argv) > 1 else "constructors.txt"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "schema.json"

    print(f"Parsing: {input_file}")
    schema = parse_tl_file(input_file)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(schema, f, indent=2, ensure_ascii=False)

    total  = len(schema["constructors"])
    types  = len(schema["grouped_by_type"])
    fields = sum(len(c["fields"]) for c in schema["constructors"])

    print(f"Done → {output_file}")
    print(f"  {total} constructors  |  {types} return types  |  {fields} total fields")


if __name__ == "__main__":
    main()