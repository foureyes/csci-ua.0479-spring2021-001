"""
syllabic_poetry.py
"""
# add your imports here


# this is a partial implementation of generate_word
# it contains a list of lists, with each sub list
# containing words with the same number of syllables
# ...the first sub list contains words with only one
# syllable, the second, two syllables, etc.
def generate_word(syllables):
    available_words = [
        ['age', 'roof', 'plain', 'slime', 'floor', 'fig', 'rode', 'oomph', 'flab', 'chit', 'creek', "we'll", 'brail', 'bay', 'big', 'salve', 'yaws', 'heal', 'bring', 'stir', 'bah', 'con', 'rone', 'team', 'nought', 'gill', 'rare', 'plains', 'bowls', 'wee', 'queue', 'gun', 'etch', 'set', 'mode', 'miss', 'ate', 'darn', 'rusk', 'mast', 'box', 'their', 'duds', 'depth', 'lien', 'rob', 'deek', 'word', 'quell', 'hark', 'home', 'pledge', 'brown', 'rune', 'pike', 'sprout', 'trace', 'cot', 'nob', 'nonce', 'dear', 'sense', 'sleek', 'poke', 'hut'],
        ['stunner', 'sucrose', 'begone', 'scorecard', 'humble', 'crouton', 'trimming', 'pudding', 'henchman', 'cackle', 'coffee', 'coma', 'aces', 'prudence', 'rematch', 'hipper', 'chopper', 'imprint', 'purple', 'second', 'lowbrow', 'faucet', 'bureau', 'commune', 'endive', 'stakeout', 'sourpuss', 'cave-in', 'shipyard', 'honors', 'kowtow', 'okra', 'haler', 'rattan'],
        ['echoless', 'fluidly', 'catchier', 'cathartic', 'lawnmower', 'physicist', 'huntedly', 'unzipping', 'centigrade', 'cheekily', 'tectonics', 'clearheaded', 'seditious', 'anodized', 'vehicle', 'sprightliest', 'prevention', 'vehement', 'mnemonics', 'steamroller', 'spikiest', 'persuasive', 'randomly', 'forensics', 'uneasy', 'dizziness', 'nonhuman', 'ethanol', 'connection', 'shrewishly', 'fingerprint'],
        ['nongalactic', 'lacerating', 'optometer', 'troglodytic', 'regradated', 'uniformize', 'chlorination', 'retotaling', 'acceptable', 'culmination', 'forbiddingness', 'immoveable', 'disconcerted', 'prosperity', 'vapourizing', 'profitably', 'envelopment', 'unsealable', 'librarian', 'transmissiveness', 'willowpattern', 'nationalise', 'devotedness', 'clangorously', 'likeableness', 'troubleshooting', 'weakheartedly', 'obsoleteness'],
        ['unsublimated', 'hyperanarchy', 'cylindrically', 'irrationally', 'quasipractical', 'sulfurization', 'undermeasuring', 'victoriously', 'disquietingly', 'metaphysical', 'quasihistoric', 'undesirably', 'soporiferous', 'underrespected', 'unsymmetrical', 'reliberating', 'curability', 'nonrevolution', 'nonscientific', 'marbleization', 'wearability', 'supervexation', 'misconjugating', 'inattentiveness', 'unruinable', 'incorporeal', 'stereoscopic', 'overpolicing', 'noncombustible', 'communicable', 'janitorial', 'etymologist', 'unconnectedness', 'personality', 'unmaintainable', 'geodesical', 'sociologist', 'fortitudinous', 'elimination'],
        ['disaffiliated', 'redeemability', 'misauthorization', 'renegotiated', 'zootomically', 'microbacteria', 'malleability', 'intermediaries', 'supportability', 'eliminatory', 'nonhierarchical', 'quasiadvantageous', 'palaeontology', 'typographically', 'radioactively', 'hyperpotassemic', 'collapsibility', 'selfdramatization', 'hallucinatory', 'megalomania', 'communicativeness', 'quasisatirical', 'nontechnological', 'electrosensitive', 'overintensity', 'excommunicating', 'fundamentality', 'photoelectrical', 'visualization', 'incommensurable', 'noncontinuity', 'etymological', 'overemotional'],
        ['electrometallurgist', 'discreditability', 'nonperfectibility', 'etherealization', 'inexhaustibility', 'unautomatically', 'overdeliberated', 'nonuniversality', 'encyclopaedically', 'paradoxicality', 'hieroglyphically', 'hypercivilization', 'biogenetically', 'incompatibility', 'unconstitutionalism', 'unutilitarian', 'overidealizing', 'transcendentalization']
        ]
