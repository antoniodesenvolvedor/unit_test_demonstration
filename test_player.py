from player import Player, Spell


class TestPlayer:
    def test_equip_spell_success(self):
        """
        Dado um jogador com nível acima de 50 e menos de 3 magias já equipadas e uma magia com nível abaixo de 10
        Quando o jogador tentar equipar uma nova magina
        Então ela deve ser equipada com sucesso
        """
        # Arrange
        player = Player(name="destroyer", level=50)
        spells = [Spell(code=1), Spell(code=2), Spell(code=3)]

        # Act / Assert
        for order, spell in enumerate(spells):
            result = player.equip_spell(spell)

            assert result is True
            assert len(player.spells) == order + 1

    def test_equip_spell_error_player_level_below_50(self):
        """
        Dado um jogador com nível abaixo de 50
        Quando o jogador tentar equipar uma nova magia
        Então ela NÂO deve ser equipada
        """
        # Arrange
        player = Player(name="destroyer", level=49)
        spell = Spell(code=1)

        # Act
        result = player.equip_spell(spell)

        # Assert
        assert result is False
        assert len(player.spells) == 0

    def test_equip_spell_error_equipping_same_spell_twice(self):
        """
        Dado um jogador tentando equipar uma mágia
        Quando o jogador já possui a mesma magia equipada
        Então ela NÂO deve ser equipada
        """
        # Arrange
        player = Player(name="destroyer", level=50)
        spell_1 = Spell(code=1)
        spell_2 = Spell(code=1)

        # Act / Assert
        result = player.equip_spell(spell_1)

        assert result is True
        assert len(player.spells) == 1

        result = player.equip_spell(spell_2)

        assert result is False
        assert len(player.spells) == 1

    def test_equip_spell_error_equipping_more_than_3_spells(self):
        """
        Dado um jogador tentando equipar uma mágia
        Quando o jogador já possui 3 magias equipadas
        Então ela NÂO deve ser equipada
        """
        # Arrange
        player = Player(name="destroyer", level=50)
        spell_1 = Spell(code=1)
        spell_2 = Spell(code=2)
        spell_3 = Spell(code=3)
        spell_4 = Spell(code=4)

        # Act / Assert
        result = player.equip_spell(spell_1)
        assert result is True
        assert len(player.spells) == 1

        result = player.equip_spell(spell_2)
        assert result is True
        assert len(player.spells) == 2

        result = player.equip_spell(spell_3)
        assert result is True
        assert len(player.spells) == 3

        result = player.equip_spell(spell_4)
        assert result is False
        assert len(player.spells) == 3
