class Television:

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''
        This function sets all of my instance variables
        '''
        self.__status = False
        self.__muted = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        This function turns the tv power on and off
        '''
        if self.__status is False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        '''
        This function mutes and unmutes the TV if the tv is on
        '''
        if self.__status:
            if self.__muted is False:
                self.__muted = True
            else:
                self.__muted = False
        else:
            self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        '''
        This function increases the tv channel when the tv is on
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        This function decreases the tv channel when the tv is on
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        This function increases the tv volume when the tv is on,
        and unmutes tv if muted
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume +=1
            else:
                pass

    def volume_down(self) -> None:
        '''
        This function decreases the tv volume when the tv is on,
        and unmutes tv if muted
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                pass

    def __str__(self) -> str:
        '''
        This function checks if the tv is muted and returns the values below
        return: power, channel, and volume values
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
