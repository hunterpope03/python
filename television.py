class Television: 
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None: 
        '''
        Method to initilize variables
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    
    def power(self) -> None: 
        '''
        Method to change the status of the TV (on\off)
        '''
        if self.__status: 
            self.__status = False
        else: 
            self.__status = True

    def mute(self) -> None: 
        '''
        Method to mute and unmute the TV
        '''
        if self.__status: 
            if self.__muted: 
                self.__muted = False
            else: 
                self.__muted = True

    def channel_up(self) -> None: 
        '''
        Method to increase the TV channel by one
        '''
        if self.__status: 
            if self.__channel != Television.MAX_CHANNEL: 
                self.__channel += 1
            else: 
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Method to decrease the TV channel by one
        '''
        if self.__status: 
            if self.__channel!= Television.MIN_CHANNEL: 
                self.__channel -= 1
            else: 
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None: 
        '''
        Method to increase the TV volume by one
        '''
        if self.__status: 
            if self.__muted: 
                self.__muted = False

            if self.__volume != Television.MAX_VOLUME: 
                self.__volume += 1
    
    def volume_down(self) -> None: 
        '''
        Method to decrease the TV volume by one
        '''
        if self.__status: 
            if self.__muted: 
                self.__muted = False

            if self.__volume != Television.MIN_VOLUME: 
                self.__volume -= 1
    
    def __str__(self) -> str: 
        '''
        Method to return the TV status 
        :return: TV status
        '''
        if self.__muted: 
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else: 
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'