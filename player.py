class Spell:
    def __init__(self, code: int):
        self.code = code

    def __eq__(self, other):
        return self.code == other.code


class Player:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level
        self.spells = []

    def equip_spell(self, spell: Spell) -> bool:
        if not self._is_player_spell_valid(spell):
            return False

        self.spells.append(spell)
        return True

    def _is_player_spell_valid(self, spell: Spell) -> bool:
        if self.level < 50:
            return False
        if len(self.spells) >= 3:
            return False
        if spell in self.spells:
            return False

        return True

