class Settings():
    ''' 存储《外星人入侵》的所有设置的类 '''

    def __init__(self):
        ''' 初始化游戏设置 '''

        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置（飞行速度）
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3    # 存储中最大子弹个数，即同时在屏幕中的子弹个数