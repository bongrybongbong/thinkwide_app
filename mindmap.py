def render_markdown(data, level=0):
    md_string = ""
    for key, value in data.items():
        md_string += '    ' * level + f"- **{key}**\n"
        if isinstance(value, list):
            for item in value:
                for item_key in item:
                    md_string += '    ' * (level + 1) + f"- {item_key}\n"
        else:
            md_string += render_markdown(value, level+1)
    return md_string
