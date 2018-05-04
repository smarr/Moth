# https://github.com/richard-roberts/PyPlot

import colorsys 
 
 
class HSVColor: 
    def __init__(self, hue, saturation, value): 
        self.hue = hue 
        self.saturation = saturation 
        self.value = value * 255 
 
    def get(self): 
        return self.hue, self.saturation, self.value 
 
    def get_rgb(self): 
        r, g, b = colorsys.hsv_to_rgb(*self.get()) 
        return int(r), int(g), int(b) 
 
    def get_hex(self): 
        r, g, b = self.get_rgb() 
        return '#%02x%02x%02x' % (int(r), int(g), int(b)) 
 
 
class RedDark(HSVColor): 
    def __init__(self): 
        super(RedDark, self).__init__(0.00, 0.61, 158 / 255) 
 
 
class RedLight(HSVColor): 
    def __init__(self): 
        super(RedLight, self).__init__(1.00, 0.61, 240 / 255) 
 
 
class YellowDark(HSVColor): 
    def __init__(self): 
        super(YellowDark, self).__init__(0.10, 0.72, 158 / 255) 
 
 
class YellowLight(HSVColor): 
    def __init__(self): 
        super(YellowLight, self).__init__(0.10, 0.71, 255 / 255) 
 
 
class BlueDark(HSVColor): 
    def __init__(self): 
        super(BlueDark, self).__init__(0.55, 0.79, 107 / 255) 
 
 
class BlueLight(HSVColor): 
    def __init__(self): 
        super(BlueLight, self).__init__(0.55, 0.78, 160 / 255) 
 
 
class GreenDark(HSVColor): 
    def __init__(self): 
        super(GreenDark, self).__init__(0.30, 0.59, 211 / 255) 
 
 
class GreenLight(HSVColor): 
    def __init__(self): 
        super(GreenLight, self).__init__(0.30, 0.59, 130 / 255) 
 
 
class BlackDark(HSVColor): 
    def __init__(self): 
        super(BlackDark, self).__init__(0.63, 0.38, 45 / 255) 
 
 
class BlackLight(HSVColor): 
    def __init__(self): 
        super(BlackLight, self).__init__(0.62, 0.38, 81 / 255) 
 
 
class GrayDark(HSVColor): 
    def __init__(self): 
        super(GrayDark, self).__init__(0.58, 0.04, 12 / 255) 
 
 
class GrayMid(HSVColor): 
    def __init__(self): 
        super(GrayMid, self).__init__(0.00, 0.00, 51 / 255) 
 
 
class GrayLight(HSVColor): 
    def __init__(self): 
        super(GrayLight, self).__init__(0.00, 0.00, 153 / 255) 
 
 
class GrayVeryLight(HSVColor): 
    def __init__(self): 
        super(GrayVeryLight, self).__init__(0.00, 0.00, 200 / 255) 
 
 
class White(HSVColor): 
    def __init__(self): 
        super(White, self).__init__(0.00, 0.00, 255 / 255) 
 
 
def get_bright_set(): 
    # https://color.adobe.com/Bright-Leaves-color-theme-10001952 
    return [HSVColor(215 / 360, 97 / 100, 35 / 100), 
            HSVColor(209 / 360, 88 / 100, 84 / 100), 
            HSVColor(45 / 360, 96 / 100, 95 / 100), 
            HSVColor(28 / 360, 99 / 100, 95 / 100), 
            HSVColor(16 / 360, 98 / 100, 95 / 100), 
            HSVColor(248 / 360, 42 / 100, 84 / 100)]