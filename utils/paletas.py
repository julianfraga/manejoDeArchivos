import seaborn as sns

def list2dictPalette(respuestas, palette="RdYlGn_r", noSabe=True):
    if noSabe:
        colors = sns.color_palette(palette, len(respuestas) - 1).as_hex()
        colors.append('#c9bebd')
    else:
        colors = sns.color_palette(palette, len(respuestas)).as_hex()
    colors = ['#fffd5e' if c == '#fffebe' else c for c in colors]
    return dict(zip(respuestas, colors))