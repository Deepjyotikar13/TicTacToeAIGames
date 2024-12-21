class ColorForText:
    Endc = '\033[0m'
    Bold= '\033[1m'
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'
if __name__=="__main__":
	print(ColorForText.Magenta+ "Warning: No active frommets remain. Continue?" + ColorForText.Endc)
	print("hrllo")