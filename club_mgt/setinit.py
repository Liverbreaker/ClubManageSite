from club_mgt.models import Club

def generate_club():
    Club.objects.create(
        name="3D列印社",
        name_eng="3D Printing Club",
        # leader="",
        # teacher="",
        # manager="",
        office="ES117",
        activity_place="國璽樓MD120",
        activity_time="每周三導師時間、每周五晚上6:30~9:30",
        fee="3500",
        web="",
        contact="",
        info="練習如何設計3D模型，列印3D模型及改進列印效率、"
    )
    Club.objects.create(
        name="羽球社",
        name_eng="Badminton Club",
        # leader="",
        # teacher="",
        # manager="",
        office="ES217",
        activity_place="中美堂內",
        activity_time="每周三導師時間、每周一晚上6:30~9:30",
        fee="800",
        web="",
        contact="王社長:0931-009900 / fb:王大富",
        info="精進羽球技巧"
    )
    Club.objects.create(
        name="熱舞社",
        name_eng="Dancing Club",
        # leader="",
        # teacher="",
        # manager="",
        office="ES317",
        activity_place="國璽樓一樓外面",
        activity_time="每周一~五晚上5:40~9:50",
        fee="1200",
        web="",
        contact="陳副社長:0978-113445 / fb:陳靜怡",
        info="練習各種街舞(Breaking, Hip-hop...)"
    )
    Club.objects.create(
        name="動漫社",
        name_eng="Anime Club",
        # leader="",
        # teacher="",
        # manager="",
        office="ES417",
        activity_place="JS121",
        activity_time="每週一、四晚上6:30~9:30",
        fee="600",
        web="",
        contact="",
        info="一起參加漫展、繪製二次元畫、COSPLAY"
    )
    Club.objects.create(
        name="吹玻璃社",
        name_eng="Glass Blowing Club",
        # leader="",
        # teacher="",
        # manager="",
        office="ES517",
        activity_place="輔園旁涼亭",
        activity_time="每週一~三早上7:00~8:00、週六10:00~17:00",
        fee="2000",
        web="",
        contact="",
        info="練習吹製漂亮的玻璃器具"
    )
    Club.objects.create(
        name="理財投資社",
        name_eng="Investment Club",
        # leader="",
        # teacher="",
        # manager="",
        office="ES617",
        activity_place="LM101",
        activity_time="每周三導師時間、周四晚上6:30~9:30",
        fee="1500",
        web="",
        contact="",
        info="邀請講師教授投資策略、開辦模擬投資比賽"
    )
    Club.objects.create(
        name="軟體開發社",
        name_eng="Software Development Club",
        # leader="",
        # teacher="",
        # manager="",
        office="ES717",
        activity_place="LE4A",
        activity_time="每周一、四晚上6:30~9:30",
        fee="1600",
        web="",
        contact="",
        info="一起開發各種軟體程式，電腦及攜帶式裝置(ios, android...)"
    )
