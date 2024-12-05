import pytest
from television import * 

class Test: 
    def setup_method(self): 
        self.tv1 = Television()

    def teardown_method(self): 
        del self.tv1

    def test_init(self): 
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv1.power() 
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0' # TV on

        self.tv1.power() 
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0' # TV off

    def test_mute(self): 
        self.tv1.power() 
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0' # TV on, volume up one, and muted

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1' # TV on and unmuted

        self.tv1.power()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1' # TV off and muted

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1' # TV off and unmuted

    def test_channel_up(self): 
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0' # TV off and channel up

        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0' # TV on and channel up

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0' # TV on and channel up past maximum 

    def test_channel_down(self): 
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0' # TV off and channel down

        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0' # TV on and channel down past minimum 

    def test_volume_up(self): 
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0' # TV off and volume up

        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1' # TV on and volume up one

        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2' # TV on, muted, and volume up one

        self.tv1.mute()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2' # TV on and volume up past maximum 

    def test_volume_down(self): 
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0' # TV off and volume down

        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1' # TV on, volume up twice, and volume down one 

        self.tv1.volume_up()
        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1' # TV on, volume up one, muted, and volume down one

        self.tv1.mute()
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0' # TV on and volume down past maximum 


