#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成全部题库数据文件"""
import json
import os
import random
import sys
from datetime import datetime, timezone, timedelta

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =========================
# 1. 古诗库（30首，适合幼儿）
# =========================
poems = [
    {"title": "咏鹅", "author": "骆宾王", "dynasty": "唐",
     "content": "鹅鹅鹅，曲项向天歌。白毛浮绿水，红掌拨清波。",
     "pinyin": "é é é，qū xiàng xiàng tiān gē。bái máo fú lǜ shuǐ，hóng zhǎng bō qīng bō。",
     "meaning": "大白鹅啊大白鹅，弯着脖子对着天空唱歌。白色的羽毛浮在绿水上，红色的脚掌拨动清清的水波。"},
    {"title": "春晓", "author": "孟浩然", "dynasty": "唐",
     "content": "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
     "pinyin": "chūn mián bù jué xiǎo，chù chù wén tí niǎo。yè lái fēng yǔ shēng，huā luò zhī duō shǎo。",
     "meaning": "春天的夜晚睡得香甜不知不觉就到了天亮，醒来时到处都能听到鸟儿的叫声。想起昨夜的风雨声，不知有多少花儿被吹落了。"},
    {"title": "静夜思", "author": "李白", "dynasty": "唐",
     "content": "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
     "pinyin": "chuáng qián míng yuè guāng，yí shì dì shàng shuāng。jǔ tóu wàng míng yuè，dī tóu sī gù xiāng。",
     "meaning": "床前明亮的月光，好像是地上的一层白霜。抬起头望着明月，低下头思念自己的故乡。"},
    {"title": "悯农", "author": "李绅", "dynasty": "唐",
     "content": "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。",
     "pinyin": "chú hé rì dāng wǔ，hàn dī hé xià tǔ。shuí zhī pán zhōng cān，lì lì jiē xīn kǔ。",
     "meaning": "农民在正午的烈日下锄禾，汗水滴入禾苗下的泥土。谁知道盘中的饭食，每一粒都是辛勤劳动的成果。"},
    {"title": "画", "author": "王维", "dynasty": "唐",
     "content": "远看山有色，近听水无声。春去花还在，人来鸟不惊。",
     "pinyin": "yuǎn kàn shān yǒu sè，jìn tīng shuǐ wú shēng。chūn qù huā hái zài，rén lái niǎo bù jīng。",
     "meaning": "远看山上有美丽的颜色，走近却听不到水流的声音。春天过去了花依然开放，人走近了鸟也不害怕。"},
    {"title": "登鹳雀楼", "author": "王之涣", "dynasty": "唐",
     "content": "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。",
     "pinyin": "bái rì yī shān jìn，huáng hé rù hǎi liú。yù qióng qiān lǐ mù，gèng shàng yī céng lóu。",
     "meaning": "太阳依着山慢慢落下，黄河水向大海流去。想要看到更远的风景，就要再爬高一层楼。"},
    {"title": "江雪", "author": "柳宗元", "dynasty": "唐",
     "content": "千山鸟飞绝，万径人踪灭。孤舟蓑笠翁，独钓寒江雪。",
     "pinyin": "qiān shān niǎo fēi jué，wàn jìng rén zōng miè。gū zhōu suō lì wēng，dú diào hán jiāng xuě。",
     "meaning": "群山中鸟儿都不见了，所有路上也没有人的踪迹。只有一个穿蓑衣戴斗笠的老爷爷，独自在寒冷的江雪中钓鱼。"},
    {"title": "咏柳", "author": "贺知章", "dynasty": "唐",
     "content": "碧玉妆成一树高，万条垂下绿丝绦。不知细叶谁裁出，二月春风似剪刀。",
     "pinyin": "bì yù zhuāng chéng yī shù gāo，wàn tiáo chuí xià lǜ sī tāo。bù zhī xì yè shuí cái chū，èr yuè chūn fēng sì jiǎn dāo。",
     "meaning": "柳树像碧玉装扮的一样高，千万条枝条像绿色丝带垂下来。不知道这细细的叶子是谁裁出来的，原来是二月的春风像剪刀一样。"},
    {"title": "草", "author": "白居易", "dynasty": "唐",
     "content": "离离原上草，一岁一枯荣。野火烧不尽，春风吹又生。",
     "pinyin": "lí lí yuán shàng cǎo，yī suì yī kū róng。yě huǒ shāo bù jìn，chūn fēng chuī yòu shēng。",
     "meaning": "原野上的草长得很茂盛，每年枯萎又茂盛。野火也烧不完它，春风一吹它又长出来了。"},
    {"title": "寻隐者不遇", "author": "贾岛", "dynasty": "唐",
     "content": "松下问童子，言师采药去。只在此山中，云深不知处。",
     "pinyin": "sōng xià wèn tóng zǐ，yán shī cǎi yào qù。zhǐ zài cǐ shān zhōng，yún shēn bù zhī chù。",
     "meaning": "在松树下问小徒弟，他说师傅去采药了。师傅就在这座山里，但云雾太深不知道在哪里。"},
    {"title": "池上", "author": "白居易", "dynasty": "唐",
     "content": "小娃撑小艇，偷采白莲回。不解藏踪迹，浮萍一道开。",
     "pinyin": "xiǎo wá chēng xiǎo tǐng，tōu cǎi bái lián huí。bù jiě cáng zōng jì，fú píng yī dào kāi。",
     "meaning": "小娃娃撑着小船，偷偷采了白莲回来。他不懂得隐藏踪迹，水面上的浮萍被船分开了一条路。"},
    {"title": "相思", "author": "王维", "dynasty": "唐",
     "content": "红豆生南国，春来发几枝。愿君多采撷，此物最相思。",
     "pinyin": "hóng dòu shēng nán guó，chūn lái fā jǐ zhī。yuàn jūn duō cǎi xié，cǐ wù zuì xiāng sī。",
     "meaning": "红豆生长在南方，春天来了长出几根新枝。希望你多采一些，这东西最能表达思念。"},
    {"title": "游子吟", "author": "孟郊", "dynasty": "唐",
     "content": "慈母手中线，游子身上衣。临行密密缝，意恐迟迟归。谁言寸草心，报得三春晖。",
     "pinyin": "cí mǔ shǒu zhōng xiàn，yóu zǐ shēn shàng yī。lín xíng mì mì féng，yì kǒng chí chí guī。shuí yán cùn cǎo xīn，bào dé sān chūn huī。",
     "meaning": "妈妈手中的针线，为出门的孩子缝衣服。临走时缝得密密麻麻，怕孩子回来得太晚。谁说小草的心意，能报答春天阳光般的母爱呢？"},
    {"title": "鹿柴", "author": "王维", "dynasty": "唐",
     "content": "空山不见人，但闻人语响。返景入深林，复照青苔上。",
     "pinyin": "kōng shān bù jiàn rén，dàn wén rén yǔ xiǎng。fǎn jǐng rù shēn lín，fù zhào qīng tái shàng。",
     "meaning": "空旷的山中看不见人，只能听到人说话的声音。夕阳的余光照进深林，又照在青苔上。"},
    {"title": "逢雪宿芙蓉山主人", "author": "刘长卿", "dynasty": "唐",
     "content": "日暮苍山远，天寒白屋贫。柴门闻犬吠，风雪夜归人。",
     "pinyin": "rì mù cāng shān yuǎn，tiān hán bái wū pín。chái mén wén quǎn fèi，fēng xuě yè guī rén。",
     "meaning": "天快黑了青山显得更远，天气寒冷茅草屋更显贫穷。柴门外听到狗叫声，是有人在风雪之夜回来了。"},
    {"title": "赠汪伦", "author": "李白", "dynasty": "唐",
     "content": "李白乘舟将欲行，忽闻岸上踏歌声。桃花潭水深千尺，不及汪伦送我情。",
     "pinyin": "lǐ bái chéng zhōu jiāng yù xíng，hū wén àn shàng tà gē shēng。táo huā tán shuǐ shēn qiān chǐ，bù jí wāng lún sòng wǒ qíng。",
     "meaning": "李白正要坐船出发，忽然听到岸上有唱歌的声音。桃花潭的水有千尺深，也比不上汪伦送我的情意深。"},
    {"title": "望庐山瀑布", "author": "李白", "dynasty": "唐",
     "content": "日照香炉生紫烟，遥看瀑布挂前川。飞流直下三千尺，疑是银河落九天。",
     "pinyin": "rì zhào xiāng lú shēng zǐ yān，yáo kàn pù bù guà qián chuān。fēi liú zhí xià sān qiān chǐ，yí shì yín hé luò jiǔ tiān。",
     "meaning": "阳光照着香炉峰生出紫色烟雾，远远看去瀑布挂在前面的山川上。水流从高处直冲下来有三千尺，让人怀疑是银河从天上落下来了。"},
    {"title": "绝句", "author": "杜甫", "dynasty": "唐",
     "content": "两个黄鹂鸣翠柳，一行白鹭上青天。窗含西岭千秋雪，门泊东吴万里船。",
     "pinyin": "liǎng gè huáng lí míng cuì liǔ，yī xíng bái lù shàng qīng tiān。chuāng hán xī lǐng qiān qiū xuě，mén bó dōng wú wàn lǐ chuán。",
     "meaning": "两只黄鹂在翠绿的柳树上唱歌，一行白鹭飞上蓝天。窗户里能看到西边山上千年不化的雪，门前停着从东吴来的万里船。"},
    {"title": "春夜喜雨", "author": "杜甫", "dynasty": "唐",
     "content": "好雨知时节，当春乃发生。随风潜入夜，润物细无声。",
     "pinyin": "hǎo yǔ zhī shí jié，dāng chūn nǎi fā shēng。suí fēng qián rù yè，rùn wù xì wú shēng。",
     "meaning": "好雨知道下雨的时节，春天来了就下起来了。跟着风悄悄地在夜里下，滋润万物细细地没有声音。"},
    {"title": "枫桥夜泊", "author": "张继", "dynasty": "唐",
     "content": "月落乌啼霜满天，江枫渔火对愁眠。姑苏城外寒山寺，夜半钟声到客船。",
     "pinyin": "yuè luò wū tí shuāng mǎn tiān，jiāng fēng yú huǒ duì chóu mián。gū sū chéng wài hán shān sì，yè bàn zhōng shēng dào kè chuán。",
     "meaning": "月亮落下乌鸦啼叫满天寒霜，江边的枫树和渔船上的灯火伴着我忧愁入眠。姑苏城外的寒山寺，半夜的钟声传到了客船上。"},
    {"title": "游园不值", "author": "叶绍翁", "dynasty": "宋",
     "content": "应怜屐齿印苍苔，小扣柴扉久不开。春色满园关不住，一枝红杏出墙来。",
     "pinyin": "yīng lián jī chǐ yìn cāng tái，xiǎo kòu chái fēi jiǔ bù kāi。chūn sè mǎn yuán guān bú zhù，yī zhī hóng xìng chū qiáng lái。",
     "meaning": "可能是怕我的木鞋踩坏了青苔，轻轻敲门很久也没人开。但满园的春色是关不住的，一枝红杏伸出了墙头来。"},
    {"title": "小池", "author": "杨万里", "dynasty": "宋",
     "content": "泉眼无声惜细流，树阴照水爱晴柔。小荷才露尖尖角，早有蜻蜓立上头。",
     "pinyin": "quán yǎn wú shēng xī xì liú，shù yīn zhào shuǐ ài qíng róu。xiǎo hé cái lù jiān jiān jiǎo，zǎo yǒu qīng tíng lì shàng tóu。",
     "meaning": "泉眼无声地珍惜着细小的水流，树荫映在水面上喜爱这晴天的温柔。小荷叶刚露出尖尖的角，蜻蜓早就停在上面了。"},
    {"title": "村居", "author": "高鼎", "dynasty": "清",
     "content": "草长莺飞二月天，拂堤杨柳醉春烟。儿童散学归来早，忙趁东风放纸鸢。",
     "pinyin": "cǎo zhǎng yīng fēi èr yuè tiān，fú dī yáng liǔ zuì chūn yān。ér tóng sàn xué guī lái zǎo，máng chèn dōng fēng fàng zhǐ yuān。",
     "meaning": "二月天草长莺飞，杨柳轻拂着堤岸好像沉醉在春天的烟雾里。孩子们放学回来得早，赶忙趁着东风放风筝。"},
    {"title": "所见", "author": "袁枚", "dynasty": "清",
     "content": "牧童骑黄牛，歌声振林樾。意欲捕鸣蝉，忽然闭口立。",
     "pinyin": "mù tóng qí huáng niú，gē shēng zhèn lín yuè。yì yù bǔ míng chán，hū rán bì kǒu lì。",
     "meaning": "牧童骑着黄牛，歌声震动了树林。他想要捕捉鸣叫的蝉，忽然闭上嘴站住了。"},
    {"title": "回乡偶书", "author": "贺知章", "dynasty": "唐",
     "content": "少小离家老大回，乡音无改鬓毛衰。儿童相见不相识，笑问客从何处来。",
     "pinyin": "shào xiǎo lí jiā lǎo dà huí，xiāng yīn wú gǎi bìn máo shuāi。ér tóng xiāng jiàn bù xiāng shí，xiào wèn kè cóng hé chù lái。",
     "meaning": "小时候离开家乡老了才回来，家乡口音没变但头发已经白了。孩子们看见我不认识，笑着问客人是从哪里来的。"},
    {"title": "凉州词", "author": "王之涣", "dynasty": "唐",
     "content": "黄河远上白云间，一片孤城万仞山。羌笛何须怨杨柳，春风不度玉门关。",
     "pinyin": "huáng hé yuǎn shàng bái yún jiān，yī piàn gū chéng wàn rèn shān。qiāng dí hé xū yuàn yáng liǔ，chūn fēng bù dù yù mén guān。",
     "meaning": "黄河远远地流向白云之间，一座孤城在万仞高山之中。羌笛何必埋怨杨柳呢，春风是吹不到玉门关的。"},
    {"title": "出塞", "author": "王昌龄", "dynasty": "唐",
     "content": "秦时明月汉时关，万里长征人未还。但使龙城飞将在，不教胡马度阴山。",
     "pinyin": "qín shí míng yuè hàn shí guān，wàn lǐ cháng zhēng rén wèi huán。dàn shǐ lóng chéng fēi jiāng zài，bù jiào hú mǎ dù yīn shān。",
     "meaning": "秦时的明月汉时的关，万里出征的人还没回来。只要有龙城飞将在，就不会让胡人的马匹越过阴山。"},
    {"title": "芙蓉楼送辛渐", "author": "王昌龄", "dynasty": "唐",
     "content": "寒雨连江夜入吴，平明送客楚山孤。洛阳亲友如相问，一片冰心在玉壶。",
     "pinyin": "hán yǔ lián jiāng yè rù wú，píng míng sòng kè chǔ shān gū。luò yáng qīn yǒu rú xiāng wèn，yī piàn bīng xīn zài yù hú。",
     "meaning": "寒雨连着江水夜里进入吴地，天亮时送别客人楚山显得孤零零。洛阳的亲友如果问起我，就说我的心像玉壶里的冰一样纯洁。"},
    {"title": "竹枝词", "author": "刘禹锡", "dynasty": "唐",
     "content": "杨柳青青江水平，闻郎江上踏歌声。东边日出西边雨，道是无晴却有晴。",
     "pinyin": "yáng liǔ qīng qīng jiāng shuǐ píng，wén láng jiāng shàng tà gē shēng。dōng biān rì chū xī biān yǔ，dào shì wú qíng què yǒu qíng。",
     "meaning": "杨柳青青江水平静，听到江上有人唱歌。东边出太阳西边下雨，说是没有晴天却又有晴天。"},
    {"title": "忆江南", "author": "白居易", "dynasty": "唐",
     "content": "江南好，风景旧曾谙。日出江花红胜火，春来江水绿如蓝。能不忆江南？",
     "pinyin": "jiāng nán hǎo，fēng jǐng jiù céng ān。rì chū jiāng huā hóng shèng huǒ，chūn lái jiāng shuǐ lǜ rú lán。néng bù yì jiāng nán？",
     "meaning": "江南真好，那里的风景我以前很熟悉。太阳出来江边的花比火还红，春天来了江水像蓝草一样绿。能不怀念江南吗？"},
    {"title": "悯农其二", "author": "李绅", "dynasty": "唐",
     "content": "春种一粒粟，秋收万颗子。四海无闲田，农夫犹饿死。",
     "pinyin": "chūn zhòng yī lì sù，qiū shōu wàn kē zǐ。sì hǎi wú xián tián，nóng fū yóu è sǐ。",
     "meaning": "春天种下一粒种子，秋天收获万颗粮食。天下没有荒废的田地，但农民还是有饿死的。"},
]


# =========================
# 2. 成语库（30个）
# =========================
idioms = [
    {"name": "守株待兔", "pinyin": "shǒu zhū dài tù",
     "meaning": "比喻不主动努力，而存万一的侥幸心理，希望得到意外的收获。",
     "story": "宋国有个农民，一天在田里干活，忽然看见一只兔子撞死在树桩上。他没费力气就捡了一只兔子，从此他不再种地，整天守在树桩旁等兔子撞死。结果再也没等到兔子，田地也荒废了。"},
    {"name": "拔苗助长", "pinyin": "bá miáo zhù zhǎng",
     "meaning": "比喻违反事物发展的客观规律，急于求成，反而把事情弄糟。",
     "story": "有个农夫觉得田里的秧苗长得太慢，就把每棵秧苗都往上拔高了一些。他回家对儿子说：今天太累了，不过我帮助秧苗长高了！儿子跑去一看，秧苗全都枯死了。"},
    {"name": "掩耳盗铃", "pinyin": "yǎn ěr dào líng",
     "meaning": "比喻自己欺骗自己，明明掩盖不住的事情偏要想法子掩盖。",
     "story": "有个小偷想去偷一口大钟。钟太大了背不动，他找来大锤想敲碎再搬。一敲钟就发出巨大的响声，他怕别人听到来抓他，就捂住自己的耳朵。他以为自己听不到别人也就听不到了。"},
    {"name": "刻舟求剑", "pinyin": "kè zhōu qiú jiàn",
     "meaning": "比喻拘泥成例，不知道跟着情势的变化而改变看法或办法。",
     "story": "楚国有个人坐船渡河，不小心把剑掉到水里了。他赶紧在船舷上刻了一个记号，说：我的剑就是从这个地方掉下去的。等船到岸了，他从刻记号的地方下水找剑，当然找不到了。"},
    {"name": "亡羊补牢", "pinyin": "wáng yáng bǔ láo",
     "meaning": "比喻出了问题以后想办法补救，可以防止继续受损失。",
     "story": "牧羊人发现羊圈破了个洞，少了一只羊。邻居劝他赶紧把洞补上，他说羊已经丢了还补什么。第二天又少了一只羊，他这才赶紧把洞补好，从此再也没丢过羊。"},
    {"name": "画蛇添足", "pinyin": "huà shé tiān zú",
     "meaning": "比喻做多余的事，反而不恰当，弄巧成拙。",
     "story": "几个人比赛画蛇，谁先画完谁喝酒。一个人先画完了，他又给蛇画上了脚。另一个人也画完了，说：蛇本来就没有脚，你画的不是蛇。结果那个人喝了酒。"},
    {"name": "井底之蛙", "pinyin": "jǐng dǐ zhī wā",
     "meaning": "比喻见识短浅的人。",
     "story": "井里住着一只青蛙，它对大海龟说：我住在这里好快乐！井里全是我的地盘。大海龟告诉它：大海大得看不到边，深得探不到底，比你的井好多了。青蛙听了很吃惊。"},
    {"name": "狐假虎威", "pinyin": "hú jiǎ hǔ wēi",
     "meaning": "比喻借着别人的威势来吓唬人。",
     "story": "老虎抓住了一只狐狸，狐狸说：你不敢吃我，天帝让我做百兽之王，不信你跟在我后面走，看看动物们怕不怕我。老虎跟着狐狸走，动物们看见老虎都跑了。老虎以为它们怕狐狸，其实是怕自己。"},
    {"name": "愚公移山", "pinyin": "yú gōng yí shān",
     "meaning": "比喻坚持不懈地改造自然和坚定不移地进行斗争。",
     "story": "愚公家门前有两座大山挡路，他决定把山挖平。智叟笑他自不量力，愚公说：我死了有儿子，儿子死了有孙子，子子孙孙无穷尽，山不会长高，总有一天会挖平的。天帝被感动，派人搬走了山。"},
    {"name": "自相矛盾", "pinyin": "zì xiāng máo dùn",
     "meaning": "比喻自己说话做事前后抵触。",
     "story": "楚国有个人卖矛和盾。他先夸盾说：我的盾什么矛都刺不穿。又夸矛说：我的矛什么盾都能刺穿。有人问他：用你的矛刺你的盾会怎样？他哑口无言。"},
    {"name": "滥竽充数", "pinyin": "làn yú chōng shù",
     "meaning": "比喻没有真才实学的人混在行家里充数。",
     "story": "齐宣王喜欢听三百人一起吹竽。南郭先生不会吹，却混在乐队里装模作样，也拿了工钱。齐宣王死后，齐湣王喜欢听人一个一个吹，南郭先生只好逃跑了。"},
    {"name": "画龙点睛", "pinyin": "huà lóng diǎn jīng",
     "meaning": "比喻在关键地方简明扼要地点明要旨，使内容更加传神。",
     "story": "张僧繇在寺庙墙上画了四条龙，都没画眼睛。人们问他为什么不画眼睛，他说画了龙就会飞走。大家不信，他就给其中两条龙画上眼睛，顿时雷电大作，两条龙飞上了天。"},
    {"name": "对牛弹琴", "pinyin": "duì niú tán qín",
     "meaning": "比喻对不懂事理的人讲道理或言事。",
     "story": "公明仪给牛弹奏高雅的曲子，牛只顾吃草根本不理。他转而弹奏类似蚊虻的声音和小牛的叫声，牛就竖起耳朵仔细听。不是琴弹得不好，是牛听不懂啊。"},
    {"name": "杯弓蛇影", "pinyin": "bēi gōng shé yǐng",
     "meaning": "比喻因疑神疑鬼而引起恐惧。",
     "story": "乐广请朋友喝酒，朋友看到杯里有条蛇，回家就病了。乐广发现墙上挂的弓映在杯里像蛇，又请朋友来喝酒，让他看清是弓的影子不是蛇。朋友明白后病就好了。"},
    {"name": "叶公好龙", "pinyin": "yè gōng hào lóng",
     "meaning": "比喻表面上爱好某事物，实际上并不真爱好。",
     "story": "叶公子高到处说自己喜欢龙，家里到处雕着龙。真龙听说了，下来看他，龙头探进窗户。叶公吓得面如土色转身就跑。他喜欢的不是真龙，只是像龙的东西罢了。"},
    {"name": "胸有成竹", "pinyin": "xiōng yǒu chéng zhú",
     "meaning": "比喻在做事之前已经拿定主意，有了完整的计划。",
     "story": "文与可画竹子非常出名，他在画竹之前，心里就已经有了竹子的完整形象，所以画得又快又好。苏轼说：所以画竹必须先在心中有了完整的竹子。"},
    {"name": "闻鸡起舞", "pinyin": "wén jī qǐ wǔ",
     "meaning": "比喻有志报国的人即时奋起。",
     "story": "祖逖和刘琨是好朋友，他们半夜听到鸡叫，祖逖说：这不是不吉利的声音。于是起床练剑。从此他们每天听到鸡叫就起床练武，后来都成了将军。"},
    {"name": "铁杵成针", "pinyin": "tiě chǔ chéng zhēn",
     "meaning": "比喻只要有毅力，再难的事情也能做成。",
     "story": "李白小时候不爱学习，一天看到一个老奶奶在磨一根铁棒。他问在做什么，老奶奶说：我要把它磨成绣花针。李白很受感动，从此发奋读书。"},
    {"name": "囊萤映雪", "pinyin": "náng yíng yìng xuě",
     "meaning": "形容家境贫困而苦读。",
     "story": "车胤家里穷买不起灯油，夏天他抓萤火虫装在纱袋里照明读书。孙康冬天买不起灯油，就借着雪的反光读书。后来两人都成了大学问家。"},
    {"name": "程门立雪", "pinyin": "chéng mén lì xuě",
     "meaning": "比喻尊敬老师，诚恳求学。",
     "story": "杨时和游酢去拜见老师程颐，程颐正在睡觉。他们不忍心打扰，就站在门外等。等程颐醒来时，门外的雪已经有一尺深了。"},
    {"name": "孟母三迁", "pinyin": "mèng mǔ sān qiān",
     "meaning": "比喻为了孩子的教育而选择良好的环境。",
     "story": "孟子小时候家住在墓地旁边，他学人家哭丧。孟母搬到了市场旁边，孟子又学人家做生意。最后孟母搬到了学校旁边，孟子开始学读书礼仪，孟母这才满意。"},
    {"name": "孔融让梨", "pinyin": "kǒng róng ràng lí",
     "meaning": "形容懂得谦让的品德。",
     "story": "孔融四岁时，家里吃梨，他总是挑小的吃。大人问他为什么，他说：我年纪小应该吃小的，大的给哥哥们吃。大家都很夸奖他。"},
    {"name": "司马光砸缸", "pinyin": "sī mǎ guāng zá gāng",
     "meaning": "形容遇事冷静、机智应变。",
     "story": "司马光小时候和小朋友玩，一个小孩掉进大水缸里。别的小孩都吓跑了，司马光搬起大石头砸破水缸，水流出来了，小孩得救了。"},
    {"name": "曹冲称象", "pinyin": "cáo chōng chēng xiàng",
     "meaning": "形容善于动脑筋想办法。",
     "story": "有人送给曹操一头大象，大家想知道有多重但秤不够大。曹冲说：把象牵到船上，记下水面到船的位置。再往船上装石头到同样位置，称石头就可以了。"},
    {"name": "悬梁刺股", "pinyin": "xuán liáng cì gǔ",
     "meaning": "形容刻苦学习。",
     "story": "孙敬读书时怕打瞌睡，把头发绑在房梁上，一低头就会被拉醒。苏秦读书困了就用锥子刺大腿，疼痛让自己清醒继续读书。"},
    {"name": "黄香温席", "pinyin": "huáng xiāng wēn xí",
     "meaning": "形容孝顺父母。",
     "story": "黄香九岁时母亲去世，他对父亲非常孝顺。夏天他给父亲扇凉枕席，冬天他先用自己的身体把被窝暖热，再让父亲睡。"},
    {"name": "卧薪尝胆", "pinyin": "wò xīn cháng dǎn",
     "meaning": "形容人刻苦自励、发奋图强。",
     "story": "越王勾践被吴国打败后，每天睡在柴草上，吃饭睡觉前都要尝一尝苦胆，提醒自己不忘耻辱。经过多年努力，终于打败了吴国。"},
    {"name": "塞翁失马", "pinyin": "sāi wēng shī mǎ",
     "meaning": "比喻坏事在一定条件下可以变成好事。",
     "story": "边塞老人的马跑到了胡人那里，大家安慰他，他说：也许是福气。后来马带了一群胡马回来了。儿子骑马摔断了腿，他说：也许是福气。后来打仗，儿子因瘸腿没被征兵而活了下来。"},
    {"name": "鹬蚌相争", "pinyin": "yù bàng xiāng zhēng",
     "meaning": "比喻双方相持不下，第三者因而得利。",
     "story": "蚌张开壳晒太阳，鹬去啄蚌的肉，蚌合上壳夹住了鹬的嘴。鹬说：今天不下雨明天不下雨你就会干死。蚌说：今天不松嘴明天不松嘴你就会饿死。渔翁过来把它们都抓走了。"},
    {"name": "南辕北辙", "pinyin": "nán yuán běi zhé",
     "meaning": "比喻行动和目的相反。",
     "story": "有人要去南方的楚国，却驾车往北走。朋友说：你去楚国应该往南走。他说：我的马很好。朋友说：马再好方向不对也不行。他说：我钱多车夫技术好。方向错了条件越好离目标越远。"},
    {"name": "东施效颦", "pinyin": "dōng shī xiào pín",
     "meaning": "比喻盲目模仿别人，效果适得其反。",
     "story": "西施心口疼，皱着眉头按着胸口走路，大家觉得很美。东施也学她皱眉捂胸，结果更丑了。有钱人看到紧闭大门不出，穷人看到拉着妻儿躲开。"},
]


# =========================
# 3. 汉字库（100字，适合幼儿识字）
# =========================
characters = [
    {"char": "天", "pinyin": "tiān", "word": "天空", "sentence": "天上有很多白云。"},
    {"char": "地", "pinyin": "dì", "word": "大地", "sentence": "大地长满了绿草。"},
    {"char": "人", "pinyin": "rén", "word": "人们", "sentence": "人们在公园里散步。"},
    {"char": "日", "pinyin": "rì", "word": "太阳", "sentence": "太阳从东边升起来。"},
    {"char": "月", "pinyin": "yuè", "word": "月亮", "sentence": "月亮弯弯像小船。"},
    {"char": "水", "pinyin": "shuǐ", "word": "喝水", "sentence": "小猫在喝水。"},
    {"char": "火", "pinyin": "huǒ", "word": "生火", "sentence": "冬天要生火取暖。"},
    {"char": "山", "pinyin": "shān", "word": "高山", "sentence": "高山上有大树。"},
    {"char": "石", "pinyin": "shí", "word": "石头", "sentence": "河边有很多石头。"},
    {"char": "木", "pinyin": "mù", "word": "木头", "sentence": "桌子是木头做的。"},
    {"char": "花", "pinyin": "huā", "word": "花朵", "sentence": "花朵开满了花园。"},
    {"char": "草", "pinyin": "cǎo", "word": "青草", "sentence": "小羊在吃青草。"},
    {"char": "树", "pinyin": "shù", "word": "大树", "sentence": "大树下可以乘凉。"},
    {"char": "鸟", "pinyin": "niǎo", "word": "小鸟", "sentence": "小鸟在树上唱歌。"},
    {"char": "鱼", "pinyin": "yú", "word": "小鱼", "sentence": "小鱼在水里游来游去。"},
    {"char": "虫", "pinyin": "chóng", "word": "小虫", "sentence": "小虫在叶子上爬。"},
    {"char": "马", "pinyin": "mǎ", "word": "白马", "sentence": "白马跑得很快。"},
    {"char": "牛", "pinyin": "niú", "word": "奶牛", "sentence": "奶牛产牛奶。"},
    {"char": "羊", "pinyin": "yáng", "word": "小羊", "sentence": "小羊咩咩叫。"},
    {"char": "大", "pinyin": "dà", "word": "大象", "sentence": "大象的鼻子长长的。"},
    {"char": "小", "pinyin": "xiǎo", "word": "小手", "sentence": "宝宝的小手真可爱。"},
    {"char": "多", "pinyin": "duō", "word": "很多", "sentence": "天上有很多星星。"},
    {"char": "少", "pinyin": "shǎo", "word": "多少", "sentence": "还剩多少个苹果？"},
    {"char": "上", "pinyin": "shàng", "word": "上面", "sentence": "书放在桌子上面。"},
    {"char": "下", "pinyin": "xià", "word": "下面", "sentence": "猫躲在桌子下面。"},
    {"char": "左", "pinyin": "zuǒ", "word": "左边", "sentence": "左手拿笔写字。"},
    {"char": "右", "pinyin": "yòu", "word": "右边", "sentence": "右手拿筷子吃饭。"},
    {"char": "前", "pinyin": "qián", "word": "前面", "sentence": "前面有一棵大树。"},
    {"char": "后", "pinyin": "hòu", "word": "后面", "sentence": "后面有一辆红色的车。"},
    {"char": "中", "pinyin": "zhōng", "word": "中间", "sentence": "中间那个是最大的。"},
    {"char": "东", "pinyin": "dōng", "word": "东方", "sentence": "太阳从东方升起。"},
    {"char": "西", "pinyin": "xī", "word": "西方", "sentence": "太阳从西方落下。"},
    {"char": "南", "pinyin": "nán", "word": "南方", "sentence": "南方天气很暖和。"},
    {"char": "北", "pinyin": "běi", "word": "北方", "sentence": "北方冬天会下雪。"},
    {"char": "春", "pinyin": "chūn", "word": "春天", "sentence": "春天花儿都开了。"},
    {"char": "夏", "pinyin": "xià", "word": "夏天", "sentence": "夏天天气很热。"},
    {"char": "秋", "pinyin": "qiū", "word": "秋天", "sentence": "秋天树叶变黄了。"},
    {"char": "冬", "pinyin": "dōng", "word": "冬天", "sentence": "冬天可以堆雪人。"},
    {"char": "风", "pinyin": "fēng", "word": "大风", "sentence": "今天风很大。"},
    {"char": "雨", "pinyin": "yǔ", "word": "下雨", "sentence": "下雨了要打伞。"},
    {"char": "云", "pinyin": "yún", "word": "白云", "sentence": "白云飘在天上。"},
    {"char": "雪", "pinyin": "xuě", "word": "下雪", "sentence": "下雪了真开心。"},
    {"char": "日", "pinyin": "rì", "word": "日子", "sentence": "今天是个好日子。"},
    {"char": "光", "pinyin": "guāng", "word": "阳光", "sentence": "阳光照在身上暖暖的。"},
    {"char": "心", "pinyin": "xīn", "word": "开心", "sentence": "今天我很开心。"},
    {"char": "手", "pinyin": "shǒu", "word": "小手", "sentence": "用小手画画。"},
    {"char": "足", "pinyin": "zú", "word": "满足", "sentence": "吃饱了很满足。"},
    {"char": "口", "pinyin": "kǒu", "word": "开口", "sentence": "请开口说话。"},
    {"char": "目", "pinyin": "mù", "word": "目光", "sentence": "妈妈的目光很温柔。"},
    {"char": "耳", "pinyin": "ěr", "word": "耳朵", "sentence": "小兔子的耳朵长长的。"},
    {"char": "头", "pinyin": "tóu", "word": "头上", "sentence": "头上戴着一顶帽子。"},
    {"char": "口", "pinyin": "kǒu", "word": "口水", "sentence": "看到好吃的流口水。"},
    {"char": "爸", "pinyin": "bà", "word": "爸爸", "sentence": "爸爸带我出去玩。"},
    {"char": "妈", "pinyin": "mā", "word": "妈妈", "sentence": "妈妈做了好吃的饭。"},
    {"char": "爷", "pinyin": "yé", "word": "爷爷", "sentence": "爷爷在花园种花。"},
    {"char": "奶", "pinyin": "nǎi", "word": "奶奶", "sentence": "奶奶给我讲故事。"},
    {"char": "哥", "pinyin": "gē", "word": "哥哥", "sentence": "哥哥比我大两岁。"},
    {"char": "姐", "pinyin": "jiě", "word": "姐姐", "sentence": "姐姐在看书。"},
    {"char": "弟", "pinyin": "dì", "word": "弟弟", "sentence": "弟弟才一岁。"},
    {"char": "妹", "pinyin": "mèi", "word": "妹妹", "sentence": "妹妹在玩娃娃。"},
    {"char": "我", "pinyin": "wǒ", "word": "我们", "sentence": "我们一起去玩吧。"},
    {"char": "你", "pinyin": "nǐ", "word": "你好", "sentence": "你好呀小朋友。"},
    {"char": "他", "pinyin": "tā", "word": "他们", "sentence": "他们在踢球。"},
    {"char": "好", "pinyin": "hǎo", "word": "好的", "sentence": "这个苹果很好吃。"},
    {"char": "美", "pinyin": "měi", "word": "美丽", "sentence": "花儿真美丽。"},
    {"char": "白", "pinyin": "bái", "word": "白色", "sentence": "小白兔白又白。"},
    {"char": "红", "pinyin": "hóng", "word": "红色", "sentence": "苹果是红色的。"},
    {"char": "黄", "pinyin": "huáng", "word": "黄色", "sentence": "香蕉是黄色的。"},
    {"char": "绿", "pinyin": "lǜ", "word": "绿色", "sentence": "树叶是绿色的。"},
    {"char": "蓝", "pinyin": "lán", "word": "蓝色", "sentence": "天空是蓝色的。"},
    {"char": "黑", "pinyin": "hēi", "word": "黑色", "sentence": "小猫是黑色的。"},
    {"char": "吃", "pinyin": "chī", "word": "吃饭", "sentence": "到时间吃饭了。"},
    {"char": "喝", "pinyin": "hē", "word": "喝水", "sentence": "口渴了多喝水。"},
    {"char": "看", "pinyin": "kàn", "word": "看书", "sentence": "我在看书。"},
    {"char": "听", "pinyin": "tīng", "word": "听话", "sentence": "宝宝要听话。"},
    {"char": "说", "pinyin": "shuō", "word": "说话", "sentence": "请大声说话。"},
    {"char": "走", "pinyin": "zǒu", "word": "走路", "sentence": "宝宝学会走路了。"},
    {"char": "跑", "pinyin": "pǎo", "word": "跑步", "sentence": "小狗在跑步。"},
    {"char": "飞", "pinyin": "fēi", "word": "飞翔", "sentence": "小鸟在天空飞翔。"},
    {"char": "坐", "pinyin": "zuò", "word": "坐下", "sentence": "请坐下休息。"},
    {"char": "站", "pinyin": "zhàn", "word": "站立", "sentence": "站立时要挺直。"},
    {"char": "一", "pinyin": "yī", "word": "一个", "sentence": "桌上有1个苹果。"},
    {"char": "二", "pinyin": "èr", "word": "两个", "sentence": "我有2只手。"},
    {"char": "三", "pinyin": "sān", "word": "三个", "sentence": "三个小朋友在玩。"},
    {"char": "四", "pinyin": "sì", "word": "四个", "sentence": "桌子有四条腿。"},
    {"char": "五", "pinyin": "wǔ", "word": "五个", "sentence": "一只手有五根手指。"},
    {"char": "六", "pinyin": "liù", "word": "六个", "sentence": "盒子里有六个蛋。"},
    {"char": "七", "pinyin": "qī", "word": "七个", "sentence": "天上有七颗星星。"},
    {"char": "八", "pinyin": "bā", "word": "八个", "sentence": "螃蟹有八条腿。"},
    {"char": "九", "pinyin": "jiǔ", "word": "九个", "sentence": "我有九块糖。"},
    {"char": "十", "pinyin": "shí", "word": "十个", "sentence": "十个手指头。"},
    {"char": "百", "pinyin": "bǎi", "word": "一百", "sentence": "一百是很大的数。"},
    {"char": "书", "pinyin": "shū", "word": "读书", "sentence": "我喜欢读书。"},
    {"char": "笔", "pinyin": "bǐ", "word": "铅笔", "sentence": "用铅笔写字。"},
    {"char": "纸", "pinyin": "zhǐ", "word": "白纸", "sentence": "在白纸上画画。"},
    {"char": "学", "pinyin": "xué", "word": "学习", "sentence": "我要好好学习。"},
    {"char": "车", "pinyin": "chē", "word": "汽车", "sentence": "汽车在路上跑。"},
    {"char": "船", "pinyin": "chuán", "word": "小船", "sentence": "小船在水上漂。"},
    {"char": "房", "pinyin": "fáng", "word": "房子", "sentence": "房子里住着人。"},
    {"char": "门", "pinyin": "mén", "word": "开门", "sentence": "请开门让我进去。"},
    {"char": "窗", "pinyin": "chuāng", "word": "窗户", "sentence": "打开窗户通风。"},
    {"char": "衣", "pinyin": "yī", "word": "衣服", "sentence": "天冷多穿衣服。"},
    {"char": "食", "pinyin": "shí", "word": "食物", "sentence": "不要浪费食物。"},
    {"char": "球", "pinyin": "qiú", "word": "皮球", "sentence": "小朋友在拍皮球。"},
]


# =========================
# 4. 数学题库
# =========================
def generate_math():
    """生成数学题库"""
    random.seed(42)
    
    # 数数题
    counting = []
    items = ["🍎", "🍌", "🍓", "🌸", "🦋", "🐠", "⭐", "🎈", "🐰", "🐱"]
    for i in range(20):
        count = random.randint(2, 10)
        emoji = random.choice(items)
        options = sorted(set([count, count+1, count-1, count+2] if count > 1 else [count, count+1, count+2, count+3]))
        counting.append({
            "type": "counting",
            "question": f"数一数下面有几个{emoji}？",
            "visual": emoji * count,
            "answer": count,
            "options": options[:4]
        })
    
    # 10以内加减法
    calculation = []
    for i in range(50):
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        op = random.choice(["+", "-"])
        if op == "+":
            result = a + b
            if result > 10:
                result = a + b - 10 if a + b > 10 else a + b
                b = result - a if result >= a else a
                result = a + b
            if result > 10:
                continue
            q = f"{a} + {b} = ?"
        else:
            if a < b:
                a, b = b, a
            result = a - b
            q = f"{a} - {b} = ?"
        
        options = sorted(set([result, max(0,result+1), max(0,result-1), max(0,result+2)]))[:4]
        if result not in options:
            options = [result] + options[:3]
        
        calculation.append({
            "type": "calculation",
            "question": q,
            "answer": result,
            "options": sorted(options)
        })
    
    # 数感星球：比大小、找规律、相邻数
    number_sense = []
    # 比大小
    for i in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        while b == a:
            b = random.randint(1, 10)
        answer = ">" if a > b else "<"
        number_sense.append({
            "type": "compare",
            "question": f"{a} ___ {b}（填 > 或 <）",
            "answer": answer,
            "options": [">", "<"]
        })
    # 找规律
    patterns = [
        {"seq": [1, 2, 3, 4, "?"], "answer": 5, "options": [4, 5, 6, 7]},
        {"seq": [2, 4, 6, 8, "?"], "answer": 10, "options": [9, 10, 11, 12]},
        {"seq": [10, 9, 8, 7, "?"], "answer": 6, "options": [5, 6, 7, 8]},
        {"seq": [1, 3, 5, 7, "?"], "answer": 9, "options": [8, 9, 10, 11]},
        {"seq": [1, 1, 2, 2, 3, "?"], "answer": 3, "options": [2, 3, 4, 5]},
        {"seq": [5, 4, 3, 2, "?"], "answer": 1, "options": [0, 1, 2, 3]},
        {"seq": [1, 4, 7, 10, "?"], "answer": 13, "options": [11, 12, 13, 14]},
        {"seq": [3, 3, 3, 3, "?"], "answer": 3, "options": [2, 3, 4, 5]},
    ]
    for p in patterns:
        number_sense.append({
            "type": "pattern",
            "question": f"找规律：{' '.join(map(str, p['seq']))}",
            "answer": p["answer"],
            "options": p["options"]
        })
    # 相邻数
    for i in range(10):
        n = random.randint(2, 9)
        number_sense.append({
            "type": "neighbor",
            "question": f"{n}的前面一个数是？",
            "answer": n - 1,
            "options": sorted([n-1, n, n+1, n+2])
        })
    
    # 思维练习：简单应用题
    word_problems = [
        {"question": "树上有3只小鸟，又飞来了2只，现在树上有几只小鸟？", "answer": 5, "options": [4, 5, 6, 7]},
        {"question": "小明有5个糖果，吃了2个，还剩几个？", "answer": 3, "options": [2, 3, 4, 5]},
        {"question": "池塘里有4条鱼，又游来了3条，一共有几条鱼？", "answer": 7, "options": [6, 7, 8, 9]},
        {"question": "小红有6朵花，送给妹妹2朵，还有几朵？", "answer": 4, "options": [3, 4, 5, 6]},
        {"question": "桌上有2个苹果和3个梨，一共有几个水果？", "answer": 5, "options": [4, 5, 6, 7]},
        {"question": "教室里有5个男孩和3个女孩，一共有几个小朋友？", "answer": 8, "options": [7, 8, 9, 10]},
        {"question": "妈妈买了10个鸡蛋，用了4个，还剩几个？", "answer": 6, "options": [5, 6, 7, 8]},
        {"question": "小华有7颗糖，分给朋友3颗，还有几颗？", "answer": 4, "options": [3, 4, 5, 6]},
        {"question": "花园里有4朵红花和2朵黄花，一共有几朵花？", "answer": 6, "options": [5, 6, 7, 8]},
        {"question": "小猫抓了3只老鼠，又抓了4只，一共抓了几只？", "answer": 7, "options": [6, 7, 8, 9]},
    ]
    thinking = []
    for w in word_problems:
        thinking.append({
            "type": "word_problem",
            "question": w["question"],
            "answer": w["answer"],
            "options": w["options"]
        })
    
    return {
        "counting": counting,
        "calculation": calculation,
        "number_sense": number_sense,
        "thinking": thinking
    }


# =========================
# 5. 逻辑思维题库
# =========================
logic_questions = [
    {"type": "classification", "category": "分类",
     "question": "下面哪个不是水果？",
     "options": ["苹果", "香蕉", "白菜", "草莓"], "answer": 2,
     "explanation": "白菜是蔬菜，其他都是水果。"},
    {"type": "classification", "category": "分类",
     "question": "下面哪个不是动物？",
     "options": ["小猫", "小狗", "汽车", "小兔"], "answer": 2,
     "explanation": "汽车是交通工具，其他都是动物。"},
    {"type": "classification", "category": "分类",
     "question": "下面哪个不是颜色？",
     "options": ["红色", "蓝色", "苹果", "黄色"], "answer": 2,
     "explanation": "苹果是水果，其他都是颜色。"},
    {"type": "classification", "category": "分类",
     "question": "下面哪个不会飞？",
     "options": ["小鸟", "蝴蝶", "小鱼", "蜜蜂"], "answer": 2,
     "explanation": "小鱼在水里游，其他都会飞。"},
    {"type": "sequence", "category": "排序",
     "question": "把下面的数从小到大排列：3, 1, 2",
     "options": ["1, 2, 3", "3, 2, 1", "2, 1, 3", "1, 3, 2"], "answer": 0,
     "explanation": "从小到大是1, 2, 3。"},
    {"type": "sequence", "category": "排序",
     "question": "把下面的数从大到小排列：2, 5, 3",
     "options": ["5, 3, 2", "2, 3, 5", "3, 2, 5", "2, 5, 3"], "answer": 0,
     "explanation": "从大到小是5, 3, 2。"},
    {"type": "sequence", "category": "排序",
     "question": "按生长顺序排列：种子、开花、发芽、结果",
     "options": ["种子→发芽→开花→结果", "种子→开花→发芽→结果", "发芽→种子→开花→结果", "结果→开花→发芽→种子"], "answer": 0,
     "explanation": "植物生长顺序：种子→发芽→开花→结果。"},
    {"type": "reasoning", "category": "推理",
     "question": "小红比小明高，小明比小华高，谁最矮？",
     "options": ["小红", "小明", "小华", "一样高"], "answer": 2,
     "explanation": "小红>小明>小华，所以小华最矮。"},
    {"type": "reasoning", "category": "推理",
     "question": "今天是星期一，明天是星期几？",
     "options": ["星期日", "星期二", "星期三", "星期五"], "answer": 1,
     "explanation": "星期一的明天是星期二。"},
    {"type": "reasoning", "category": "推理",
     "question": "如果天下雨了，地上会怎样？",
     "options": ["变干", "变湿", "变热", "不变"], "answer": 1,
     "explanation": "下雨天地会变湿。"},
    {"type": "reasoning", "category": "推理",
     "question": "猫喜欢吃什么？",
     "options": ["草", "鱼", "石头", "树叶"], "answer": 1,
     "explanation": "猫喜欢吃鱼。"},
    {"type": "difference", "category": "找不同",
     "question": "找不同：🍎🍎🍎🍐🍎🍎，哪个不一样？",
     "options": ["第1个", "第3个", "第4个", "第6个"], "answer": 2,
     "explanation": "第4个是梨，其他都是苹果。"},
    {"type": "difference", "category": "找不同",
     "question": "找不同：🐶🐶🐱🐶🐶，哪个不一样？",
     "options": ["第1个", "第2个", "第3个", "第5个"], "answer": 2,
     "explanation": "第3个是猫，其他都是狗。"},
    {"type": "difference", "category": "找不同",
     "question": "找不同：🔴🔴🔴🔴🔵🔴，哪个不一样？",
     "options": ["第2个", "第4个", "第5个", "第6个"], "answer": 2,
     "explanation": "第5个是蓝色，其他都是红色。"},
    {"type": "reasoning", "category": "推理",
     "question": "白天太阳出来了，晚上什么出来？",
     "options": ["太阳", "月亮", "彩虹", "闪电"], "answer": 1,
     "explanation": "晚上月亮出来。"},
    {"type": "reasoning", "category": "推理",
     "question": "冬天很冷，我们要穿什么？",
     "options": ["短袖", "裙子", "棉袄", "拖鞋"], "answer": 2,
     "explanation": "冬天要穿棉袄保暖。"},
    {"type": "classification", "category": "分类",
     "question": "下面哪个是文具？",
     "options": ["苹果", "铅笔", "小狗", "衣服"], "answer": 1,
     "explanation": "铅笔是文具，用来写字。"},
    {"type": "sequence", "category": "排序",
     "question": "一天的时间顺序：上午、下午、晚上，正确的是？",
     "options": ["晚上→上午→下午", "上午→下午→晚上", "下午→上午→晚上", "上午→晚上→下午"], "answer": 1,
     "explanation": "一天顺序是上午→下午→晚上。"},
    {"type": "reasoning", "category": "推理",
     "question": "哪个动物生活在水里？",
     "options": ["小鸟", "小鱼", "小猫", "小鸡"], "answer": 1,
     "explanation": "小鱼生活在水里。"},
    {"type": "reasoning", "category": "推理",
     "question": "哪个不是交通工具？",
     "options": ["汽车", "飞机", "苹果", "船"], "answer": 2,
     "explanation": "苹果是水果，不是交通工具。"},
    {"type": "classification", "category": "分类",
     "question": "下面哪个是蔬菜？",
     "options": ["草莓", "西瓜", "胡萝卜", "葡萄"], "answer": 2,
     "explanation": "胡萝卜是蔬菜，其他都是水果。"},
    {"type": "reasoning", "category": "推理",
     "question": "夏天很热，我们经常吃什么解暑？",
     "options": ["火锅", "冰淇淋", "热汤", "烤红薯"], "answer": 1,
     "explanation": "夏天吃冰淇淋可以解暑降温。"},
    {"type": "sequence", "category": "排序",
     "question": "按年龄从小到大排：爷爷、爸爸、宝宝",
     "options": ["爷爷→爸爸→宝宝", "宝宝→爸爸→爷爷", "爸爸→宝宝→爷爷", "宝宝→爷爷→爸爸"], "answer": 1,
     "explanation": "宝宝最小，爸爸中间，爷爷最大。"},
    {"type": "difference", "category": "找不同",
     "question": "找不同：🚗🚗🚗🚌🚗，哪个不一样？",
     "options": ["第1个", "第3个", "第4个", "第5个"], "answer": 2,
     "explanation": "第4个是公交车，其他都是小汽车。"},
    {"type": "reasoning", "category": "推理",
     "question": "小鸡的妈妈是谁？",
     "options": ["鸭妈妈", "鸡妈妈", "鹅妈妈", "鸟妈妈"], "answer": 1,
     "explanation": "小鸡的妈妈是母鸡。"},
    {"type": "classification", "category": "分类",
     "question": "下面哪个不是食物？",
     "options": ["面包", "牛奶", "玩具", "鸡蛋"], "answer": 2,
     "explanation": "玩具不能吃，其他都是食物。"},
    {"type": "reasoning", "category": "推理",
     "question": "天黑了看不清楚东西，我们应该打开什么？",
     "options": ["风扇", "台灯", "水龙头", "冰箱"], "answer": 1,
     "explanation": "天黑要开灯才能看清楚。"},
    {"type": "difference", "category": "找不同",
     "question": "找不同：🌞🌞🌙🌞🌞，哪个不一样？",
     "options": ["第1个", "第2个", "第3个", "第5个"], "answer": 2,
     "explanation": "第3个是月亮，其他都是太阳。"},
    {"type": "reasoning", "category": "推理",
     "question": "小兔子喜欢吃什么？",
     "options": ["肉", "鱼", "胡萝卜", "骨头"], "answer": 2,
     "explanation": "小兔子爱吃胡萝卜。"},
    {"type": "sequence", "category": "排序",
     "question": "做饭的正确顺序：洗菜、切菜、炒菜、吃饭",
     "options": ["切菜→洗菜→炒菜→吃饭", "洗菜→切菜→炒菜→吃饭", "炒菜→洗菜→切菜→吃饭", "洗菜→炒菜→切菜→吃饭"], "answer": 1,
     "explanation": "做饭顺序：洗菜→切菜→炒菜→吃饭。"},
    {"type": "classification", "category": "分类",
     "question": "下面哪个是运动项目？",
     "options": ["跑步", "睡觉", "吃饭", "看电视"], "answer": 0,
     "explanation": "跑步是运动，其他不是。"},
    {"type": "reasoning", "category": "推理",
     "question": "雨天出门需要带什么？",
     "options": ["扇子", "雨伞", "太阳镜", "帽子"], "answer": 1,
     "explanation": "下雨天要带雨伞，才不会淋湿。"},
    {"type": "difference", "category": "找不同",
     "question": "找不同：👟👟👠👟👟，哪个不一样？",
     "options": ["第1个", "第2个", "第3个", "第4个"], "answer": 2,
     "explanation": "第3个是高跟鞋，其他都是运动鞋。"},
    {"type": "reasoning", "category": "推理",
     "question": "用什么可以把纸剪开？",
     "options": ["尺子", "剪刀", "铅笔", "橡皮"], "answer": 1,
     "explanation": "剪刀可以用来剪纸。"},
]


# =========================
# 6. 热榜数据（从已有项目复制）
# =========================
def fetch_hotboard():
    """抓取热榜数据"""
    import requests
    
    API_DOUYIN = "https://uapis.cn/api/v1/misc/hotboard?type=douyin"
    API_WEIBO = "https://uapis.cn/api/v1/misc/hotboard?type=weibo"
    
    hot_topics = []
    
    for url, platform in [(API_DOUYIN, "抖音"), (API_WEIBO, "微博")]:
        try:
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            for item in data.get("list", [])[:15]:
                hot_topics.append({
                    "title": item.get("title", ""),
                    "rank": item.get("index", 0),
                    "platform": platform,
                    "hot_value": item.get("hot_value", ""),
                    "url": item.get("url", "")
                })
        except Exception as e:
            print(f"  [{platform}] 失败: {e}", file=sys.stderr)
    
    # 去重
    seen = set()
    unique = []
    for t in hot_topics:
        if t["title"] not in seen:
            seen.add(t["title"])
            unique.append(t)
    
    return unique[:15]


def generate_inspiration(hot_topics):
    """生成创作灵感"""
    ideas_templates = [
        "从「{title}」找到创作灵感：{angle}",
        "热榜「{title}」可以这样二创：{angle}",
        "「{title}」给你的创作方向：{angle}",
        "借势「{title}」：{angle}",
        "「{title}」火了，你可以这样拍：{angle}",
    ]
    angles = ["反转视角", "情感共鸣", "实用教程", "趣味挑战", "深度解读",
              "对比测评", "情景演绎", "知识科普", "街采互动", "创意混剪"]
    
    ideas = []
    remix = []
    
    for i in range(10):
        hot = hot_topics[i % len(hot_topics)] if hot_topics else {"title": "今日热点", "platform": "全网"}
        tmpl = random.choice(ideas_templates)
        angle = random.choice(angles)
        
        ideas.append({
            "title": tmpl.replace("{title}", hot["title"]).replace("{angle}", angle),
            "source": hot["platform"],
            "desc": f"基于「{hot['title']}」| {angle}"
        })
        
        remix.append({
            "title": f"用「{angle}」方式改写「{hot['title']}」",
            "angle": angle,
            "desc": f"二创角度：{angle} | 来源：{hot['platform']}"
        })
    
    return {"ideas": ideas, "remix": remix}


# =========================
# 主函数
# =========================
def main():
    print("=" * 50, file=sys.stderr)
    print("小潘工作台 - 生成题库数据", file=sys.stderr)
    print("=" * 50, file=sys.stderr)
    
    # 1. 古诗
    print("\n[1/6] 生成古诗库...", file=sys.stderr)
    with open(os.path.join(OUTPUT_DIR, "poems.json"), "w", encoding="utf-8") as f:
        json.dump({"poems": poems}, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {len(poems)} 首古诗", file=sys.stderr)
    
    # 2. 成语
    print("\n[2/6] 生成成语库...", file=sys.stderr)
    with open(os.path.join(OUTPUT_DIR, "idioms.json"), "w", encoding="utf-8") as f:
        json.dump({"idioms": idioms}, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {len(idioms)} 个成语", file=sys.stderr)
    
    # 3. 汉字
    print("\n[3/6] 生成汉字库...", file=sys.stderr)
    with open(os.path.join(OUTPUT_DIR, "characters.json"), "w", encoding="utf-8") as f:
        json.dump({"characters": characters}, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {len(characters)} 个汉字", file=sys.stderr)
    
    # 4. 数学
    print("\n[4/6] 生成数学题库...", file=sys.stderr)
    math_data = generate_math()
    with open(os.path.join(OUTPUT_DIR, "math.json"), "w", encoding="utf-8") as f:
        json.dump(math_data, f, ensure_ascii=False, indent=2)
    total = sum(len(v) for v in math_data.values())
    print(f"  ✅ {total} 道数学题", file=sys.stderr)
    
    # 5. 逻辑思维
    print("\n[5/6] 生成逻辑思维题库...", file=sys.stderr)
    with open(os.path.join(OUTPUT_DIR, "logic.json"), "w", encoding="utf-8") as f:
        json.dump({"questions": logic_questions}, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {len(logic_questions)} 道逻辑题", file=sys.stderr)
    
    # 6. 热榜
    print("\n[6/6] 抓取热榜数据...", file=sys.stderr)
    try:
        hot = fetch_hotboard()
        inspiration = generate_inspiration(hot)
        bj_tz = timezone(timedelta(hours=8))
        now = datetime.now(bj_tz)
        hotboard_data = {
            "date": now.strftime("%Y-%m-%d"),
            "updatedAt": now.isoformat(),
            "hotTopics": hot,
            "inspiration": inspiration
        }
    except Exception as e:
        print(f"  ⚠️ 热榜抓取失败: {e}", file=sys.stderr)
        hotboard_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "updatedAt": datetime.now().isoformat(),
            "hotTopics": [{"title": "暂无热榜数据", "platform": "全网", "rank": 1}],
            "inspiration": {"ideas": [], "remix": []}
        }
    
    with open(os.path.join(OUTPUT_DIR, "hotboard.json"), "w", encoding="utf-8") as f:
        json.dump(hotboard_data, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {len(hotboard_data['hotTopics'])} 条热榜", file=sys.stderr)
    
    print(f"\n✅ 全部数据已保存到: {OUTPUT_DIR}", file=sys.stderr)


if __name__ == "__main__":
    main()
