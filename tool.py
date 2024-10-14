import re
import json

def parse_value(value):
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value.strip('"')
    if value.startswith('{{') and value.endswith('}}'):
        return json.loads(value.replace('{', '[').replace('}', ']'))
    if value.startswith('{') and value.endswith('}'):
        return list(map(int, value.strip('{}').split(',')))
    try:
        return int(value)
    except ValueError:
        return value

def parse_entry(entry):
    entry = entry.strip()
    key = re.match(r'\[(\d+)\]', entry).group(1)
    value = re.search(r'\{(.*)\}', entry, re.DOTALL).group(1)
    value = re.findall(r'(\w+)\s*=\s*(.*?),\n', value, re.DOTALL)
    entry_dict = {k: parse_value(v) for k, v in value}
    return int(key), entry_dict

def convert_to_json(data):
    entries = re.findall(r'\[\d+\]\s*=\s*\{.*?\},', data, re.DOTALL)
    result = {}
    for entry in entries:
        key, value = parse_entry(entry)
        result[key] = value
    return json.dumps(result, ensure_ascii=False, indent=4)

data = '''
{
	[10000] = 
	{
		ID = 10000,
		MonsterID = 1,
		Name = "白刀队",
		DescTitle = "初步压制策略",
		DescText = "<Text_3_W>为维护善见城统治秩序招募的基本作战人员，在赛博空间内以同样的数字形象示人，使用</><Text_3_T>钝刀</><Text_3_W>痛击一切不服管理的作乱分子——至少他们期待的是这样。</>",
		FileImg = "T_TXZ_D_02",
	},
	[10001] = 
	{
		ID = 10001,
		MonsterID = 1,
		Name = "白刀队",
		DescTitle = "轻量装备方案",
		DescText = "<Text_3_W>白刀队成员制式装备仅包括一套</><Text_3_T>仿凯夫拉纤维装甲与一把未开刃的镇暴刀</><Text_3_W>，「白刀」之名便来自于此，至于其效用据观察并不理想。</>",
		FileImg = "T_TXZ_D_02",
	},
	[10002] = 
	{
		ID = 10002,
		MonsterID = 1,
		Name = "白刀队",
		DescTitle = "简化招募原则",
		DescText = "<Text_3_W>「喂，我想加入白刀队！」</>\n<Text_3_W>「你？看你这样子，蛮力是有的，会用刀吗？」</>\n<Text_3_W>「不会，但是</><Text_3_T>殴打普通人</><Text_3_W>我还是绰绰有余的。」</>\n<Text_3_W>「好，你被录用了。」</>",
		FileImg = "T_TXZ_D_02",
	},
	[10003] = 
	{
		ID = 10003,
		MonsterID = 1,
		Name = "白刀队",
		DescTitle = "执勤规章1",
		DescText = "<Text_3_W>第一条：想成为一名好的白刀队员很简单，你只需要铺好床、站笔直，以及最重要的，不管回答长官什么问题，都要先大声讲</><Text_3_T>「是！长官！」</>",
		FileImg = "T_TXZ_D_02",
	},
	[10004] = 
	{
		ID = 10004,
		MonsterID = 1,
		Name = "白刀队",
		DescTitle = "善见笑话大全1",
		DescText = "<Text_3_W>——问：一个优秀的白刀队员是什么样的？</>\n<Text_3_W>——答：他很聪明，知道用钝刀打人，同时又没有聪明到知道自己磨磨刀。</>",
		FileImg = "T_TXZ_D_02",
	},
	[10005] = 
	{
		ID = 10005,
		MonsterID = 1,
		Name = "白刀队",
		DescTitle = "赛博作战手册1",
		DescText = "<Text_3_W>白刀队员是任劳任怨的一线作战人员，这也意味着在赛博空间内对他们进行精神打击是十分简单和有效的：比如询问他们</><Text_3_T>有没有加班费、什么时候转正</><Text_3_W>等等，有一定概率会导致白刀队员不战而走。</>",
		FileImg = "T_TXZ_D_02",
	},
	[10006] = 
	{
		ID = 10006,
		MonsterID = 2,
		Name = "破障队",
		DescTitle = "有限压制策略",
		DescText = "<Text_3_W>为维护善见城统治秩序招募的基本作战人员，使用</><Text_3_T>重型破障工具</><Text_3_W>作为武器。在面对大规模街垒阻挡时十分有效（目前尚未遇到过这种情况）。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10007] = 
	{
		ID = 10007,
		MonsterID = 2,
		Name = "破障队",
		DescTitle = "重型装备方案",
		DescText = "<Text_3_W>装备有</><Text_3_T>加重的凯夫拉装甲</><Text_3_W>，一般意义上的冷兵器很难对他们造成伤害，他们也借此横行霸道。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10008] = 
	{
		ID = 10008,
		MonsterID = 2,
		Name = "破障队",
		DescTitle = "特别招募原则",
		DescText = "<Text_3_W>对身高、体重与体脂率有相当要求，要求丰富的街头斗殴经验，心理评估结果为</><Text_3_T>「具暴力倾向」</><Text_3_W>者可破格录取。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10009] = 
	{
		ID = 10009,
		MonsterID = 2,
		Name = "破障队",
		DescTitle = "执勤规章2",
		DescText = "<Text_3_W>第二条：不要将破障工具使用在不相符的场合，比如吵闹的隔壁邻居、占用自己车位的车子、</><Text_3_T>善见城城墙</><Text_3_W>等处。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10010] = 
	{
		ID = 10010,
		MonsterID = 2,
		Name = "破障队",
		DescTitle = "善见笑话大全2",
		DescText = "<Text_3_W>——问：破障队员最脆弱的时候是什么时候？</>\n<Text_3_W>——答：任何时候，所以他从不放下手里的家伙事。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10011] = 
	{
		ID = 10011,
		MonsterID = 2,
		Name = "破障队",
		DescTitle = "赛博作战手册2",
		DescText = "<Text_3_W>与破障队员交战时切忌站在原地，用灵活的身段躲避其笨拙的打击是最优选择：这同样会激怒他们，切记。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10012] = 
	{
		ID = 10012,
		MonsterID = 3,
		Name = "雷震队",
		DescTitle = "特别压制策略",
		DescText = "<Text_3_W>为维护善见城统治秩序招募的特种作战人员，装备有</><Text_3_T>广域驱散武器</><Text_3_W>以应对可能的大规模暴乱。伤亡情况不在其考量范围之内。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10013] = 
	{
		ID = 10013,
		MonsterID = 3,
		Name = "雷震队",
		DescTitle = "爆破装备方案",
		DescText = "<Text_3_W>雷震队携带</><Text_3_T>「轰天雷」高爆榴弹32颗，榴弹发射器一具</><Text_3_W>。精准尚可，但威力不足。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10014] = 
	{
		ID = 10014,
		MonsterID = 3,
		Name = "雷震队",
		DescTitle = "专门招募方案",
		DescText = "<Text_3_W>三种爆炸物实用技能评定，每月安全操作细则考核，情绪稳定度测试</><Text_3_T>（非必须）</><Text_3_W>。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10015] = 
	{
		ID = 10015,
		MonsterID = 3,
		Name = "雷震队",
		DescTitle = "执勤规章3",
		DescText = "<Text_3_W>第三条：榴弹的伤害原理不尽相同，破片、金属射流、冲击波、烟雾等等都会造成伤害，但其中最重要也最致命的，是</><Text_3_T>一颗敢于使用它的心</><Text_3_W>。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10016] = 
	{
		ID = 10016,
		MonsterID = 3,
		Name = "雷震队",
		DescTitle = "善见笑话大全3",
		DescText = "<Text_3_W>——问：最适合雷震队退役后的工作是什么？</>\n<Text_3_W>——答：不需要。他们的队友不会让他们有活着退役的机会。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10017] = 
	{
		ID = 10017,
		MonsterID = 3,
		Name = "雷震队",
		DescTitle = "赛博作战手册3",
		DescText = "<Text_3_W>雷震队的榴弹由延时引信触发，其本意是给友军及时躲避的时间——这同样是我们躲避爆炸波及的好机会。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10018] = 
	{
		ID = 10018,
		MonsterID = 4,
		Name = "光铳队",
		DescTitle = "最终压制策略",
		DescText = "<Text_3_W>为维护善见城统治秩序招募的特种作战人员，接受全套</><Text_3_T>粒子束武器</><Text_3_W>使用训练，五次射击三次上靶即为合格。因为如此，绝不能小看他们可能造成的破坏。</>",
	},
	[10019] = 
	{
		ID = 10019,
		MonsterID = 4,
		Name = "光铳队",
		DescTitle = "射击装备方案",
		DescText = "<Text_3_W>装备电池供电的</><Text_3_T>「优」式粒子束步枪</><Text_3_W>，因此并未在他们的制服上设计口袋，导致大量差评。</>",
	},
	[10020] = 
	{
		ID = 10020,
		MonsterID = 4,
		Name = "光铳队",
		DescTitle = "优选招募方案",
		DescText = "<Text_3_W>招募条件非常苛刻，要求不戴眼镜，</><Text_3_T>隐形眼镜也不行</><Text_3_W>。</>",
	},
	[10021] = 
	{
		ID = 10021,
		MonsterID = 4,
		Name = "光铳队",
		DescTitle = "执勤规章4",
		DescText = "<Text_3_W>第四条：保养好你的武器，你的「优」式步枪，她由绀田兵工厂制造，把她当成</><Text_3_T>你的妻子、你的信仰、你生命的一部分</><Text_3_W>！</>",
	},
	[10022] = 
	{
		ID = 10022,
		MonsterID = 4,
		Name = "光铳队",
		DescTitle = "善见笑话大全4",
		DescText = "<Text_3_W>一个预备光铳队员正在擦拭武器，他的教官看见了，大喝道：</>\n<Text_3_W>「天哪，*文明善见*，你是我们连队的卫生楷模！要不是因为我们这里人手不足，我一定要推荐你上*文明善见*军官预备学院！你有朝一日能够做个将军！」</>\n<Text_3_W>「可我只是擦了个枪，长官。」</>\n<Text_3_W>「天哪，*文明善见*！这还不够吗？」</>",
	},
	[10023] = 
	{
		ID = 10023,
		MonsterID = 4,
		Name = "光铳队",
		DescTitle = "赛博作战手册4",
		DescText = "<Text_3_W>光铳队员普遍配备红色激光进行辅助瞄准，一旦注意到视野内</><Text_3_T>红光闪烁</><Text_3_W>，不要迟疑，马上躲避！</>",
	},
	[10024] = 
	{
		ID = 10024,
		MonsterID = 5,
		Name = "白刀队长",
		DescTitle = "初步压制策略（特）",
		DescText = "<Text_3_W>为维护善见城统治秩序招募的基本作战人员，在赛博空间内以同样的数字形象示人，使用钝刀痛击一切不服管理的作乱分子。这一职位一般由</><Text_3_T>白刀队成员的教官</><Text_3_W>担任。</>",
		FileImg = "T_TXZ_D_02",
	},
	[10025] = 
	{
		ID = 10025,
		MonsterID = 5,
		Name = "白刀队长",
		DescTitle = "武力降级",
		DescText = "<Text_3_W>白刀队的诞生来自天人仪会对数百年来城市冲突经验的总结：直接使用火器往往会导致局势快速升温，无声的冷兵器可以</><Text_3_T>有效降低作战对象的警觉度</><Text_3_W>，令白刀队可以快速瓦解尚未成型的大规模暴动。</>",
		FileImg = "T_TXZ_D_02",
	},
	[10026] = 
	{
		ID = 10026,
		MonsterID = 5,
		Name = "白刀队长",
		DescTitle = "流行歌谣",
		DescText = "<Text_3_W>善见城的城垣上，军装多鲜艳，</>\n<Text_3_W>白色的刀刃反射着阳光的金线，</>\n<Text_3_W>我们的敌人一触即溃，像风一般逃散，</>\n<Text_3_T>万岁！天人议会万岁！</>\n<Text_3_T>我们将您的权威和意志保卫！</>",
		FileImg = "T_TXZ_D_02",
	},
	[10027] = 
	{
		ID = 10027,
		MonsterID = 5,
		Name = "白刀队长",
		DescTitle = "执勤规章5",
		DescText = "<Text_3_W>第五条：执行任务时应当牢记，</><Text_3_T>逃跑的是犯罪分子，不逃跑的是训练有素意志坚定的犯罪分子</><Text_3_W>，务必严格执勤。</>",
		FileImg = "T_TXZ_D_02",
	},
	[10028] = 
	{
		ID = 10028,
		MonsterID = 5,
		Name = "白刀队长",
		DescTitle = "善见笑话大全5",
		DescText = "<Text_3_W>一群白刀队员正在练习「文明执勤」，训练内容是用钝刀打一个南瓜，但又不能打碎。队员们挨个尝试了一遍，全都打碎了。带队的白刀队长非常生气，吼道：</>\n<Text_3_W>「一群废物，看我给你们做示范。」</>\n<Text_3_W>队长一刀下去，把南瓜打个稀碎。</>\n<Text_3_W>「看见了吗，你们就是这么做的！你们就是这样对待市民吗？快给我做俯卧撑！」</>",
		FileImg = "T_TXZ_D_02",
	},
	[10029] = 
	{
		ID = 10029,
		MonsterID = 5,
		Name = "白刀队长",
		DescTitle = "赛博作战手册5",
		DescText = "<Text_3_W>不建议在白刀队长身后还有其他远程单位时与他交锋，这往往会中了他们意图将你拖在原地的圈套。</><Text_3_T>优先处理他们身后的远程单位，然后再与白刀队长进行一对一的公平战斗</><Text_3_W>，他们往往十分乐意。</>",
		FileImg = "T_TXZ_D_02",
	},
	[10030] = 
	{
		ID = 10030,
		MonsterID = 6,
		Name = "破障队长",
		DescTitle = "有限压制策略（特）",
		DescText = "<Text_3_W>为维护善见城统治秩序招募的基本作战人员，使用重型破障工具作为武器。享有</><Text_3_T>无限的蛋白粉供给与每日强制12小时健身房课程</><Text_3_W>。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10031] = 
	{
		ID = 10031,
		MonsterID = 6,
		Name = "破障队长",
		DescTitle = "主动策略",
		DescText = "<Text_3_W>为更大规模的出击提供条件，破障队常常作为叫阵的前锋</><Text_3_T>向敌人挑衅</><Text_3_W>——他们能够解决的问题都不算问题，否则便需要更具破坏性的力量出动了。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10032] = 
	{
		ID = 10032,
		MonsterID = 6,
		Name = "破障队长",
		DescTitle = "钢铁之锤",
		DescText = "<Text_3_W>「没人能战胜这最简单的暴力，</><Text_3_T>放弃抵抗！放弃幻想！放弃希望！马上投降！</><Text_3_W>」</>",
		FileImg = "T_TXZ_B_03",
	},
	[10033] = 
	{
		ID = 10033,
		MonsterID = 6,
		Name = "破障队长",
		DescTitle = "执勤规章6",
		DescText = "<Text_3_W>第六条：在媒体面前务必注意控制损害范围，非必要的暴力行为会招致禁闭处罚，禁闭场地将安排在</><Text_3_T>健身房</><Text_3_W>。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10034] = 
	{
		ID = 10034,
		MonsterID = 6,
		Name = "破障队长",
		DescTitle = "善见笑话大全6",
		DescText = "<Text_3_W>善见网络上流传着一句专门形容破障队长们的谚语：「光长腱子，不长脑子。」请务必不要在相关人员面前提起此句，以免引起人身与财产损失。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10035] = 
	{
		ID = 10035,
		MonsterID = 6,
		Name = "破障队长",
		DescTitle = "赛博作战手册6",
		DescText = "<Text_3_W>一旦破障队长做出高举武器的动作，</><Text_3_T>不要犹豫，马上跑远</><Text_3_W>，这一击带来的巨大冲击波绝对不会让人好受。</>",
		FileImg = "T_TXZ_B_03",
	},
	[10036] = 
	{
		ID = 10036,
		MonsterID = 7,
		Name = "雷震队长",
		DescTitle = "特别压制策略（特）",
		DescText = "<Text_3_W>为维护善见城统治秩序招募的特种作战人员，装备有广域驱散武器以应对可能的大规模暴乱。一般成员使用的减装药爆炸物被提升为</><Text_3_T>双倍装药</><Text_3_W>。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10037] = 
	{
		ID = 10037,
		MonsterID = 7,
		Name = "雷震队长",
		DescTitle = "附带损失",
		DescText = "<Text_3_W>雷震队出击时往往会为周遭环境造成巨大破坏，尽管面对多方指责，天人议会仍然坚持维持他们的存在，在他们看来，</><Text_3_T>与这种强大火力相称的威胁始终存在</><Text_3_W>。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10038] = 
	{
		ID = 10038,
		MonsterID = 7,
		Name = "雷震队长",
		DescTitle = "箴言一则",
		DescText = "<Text_3_W>「我是雷震队长，我是你的朋友，</><Text_3_T>但当我的榴弹射出时，我们便不再是了。</><Text_3_W>」</>",
		FileImg = "T_TXZ_R_01",
	},
	[10039] = 
	{
		ID = 10039,
		MonsterID = 7,
		Name = "雷震队长",
		DescTitle = "执勤规章7",
		DescText = "<Text_3_W>第七条：</><Text_3_T>歼灭敌有生力量是雷震队行动的最高准则</><Text_3_W>，为达成这一点，可以让友军单位做出</><Text_3_T>任何牺牲</><Text_3_W>。他们已经做好一切心理准备。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10040] = 
	{
		ID = 10040,
		MonsterID = 7,
		Name = "雷震队长",
		DescTitle = "善见笑话大全7",
		DescText = "<Text_3_W>——问：一个优秀的雷震队长在榴弹使用方面应当掌握哪三项重要技能？</>\n<Text_3_W>——答：发射前快速瞄准，发射中及时告知，善后时诚恳慰问。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10041] = 
	{
		ID = 10041,
		MonsterID = 7,
		Name = "雷震队长",
		DescTitle = "赛博作战手册7",
		DescText = "<Text_3_W>雷震队长的榴弹冲击范围</><Text_3_T>显著增加</><Text_3_W>，这要求你除了时刻保持警惕外，也要在个人防护上下些功夫，毕竟我们不是每次都能顺利脱身。</>",
		FileImg = "T_TXZ_R_01",
	},
	[10042] = 
	{
		ID = 10042,
		MonsterID = 8,
		Name = "光铳队长",
		DescTitle = "最终压制策略（特）",
		DescText = "<Text_3_W>为维护善见城统治秩序招募的特种作战人员，接受全套粒子束武器使用训练，需在季度射击考核中连续四次获得90分以上方可晋升为队长。他们的出现，</><Text_3_T>预示着局势已经无可挽回</><Text_3_W>。</>",
	},
	[10043] = 
	{
		ID = 10043,
		MonsterID = 8,
		Name = "光铳队长",
		DescTitle = "行刑执照",
		DescText = "<Text_3_W>相当一部分光铳队员在执行任务时会出现心慌、恐惧、畏缩等状况，这意味着他们良知尚存，知晓手中武器将会带来伤害与死亡。</><Text_3_T>还有一部分没有这些反应的，他们是优秀的光铳队员</><Text_3_W>。</>",
	},
	[10044] = 
	{
		ID = 10044,
		MonsterID = 8,
		Name = "光铳队长",
		DescTitle = "生存秘诀",
		DescText = "<Text_3_W>「当你的枪管过热时，与其傻站着等待降温，不如</><Text_3_T>先让白刀队顶在前面</><Text_3_W>。」</>",
	},
	[10045] = 
	{
		ID = 10045,
		MonsterID = 8,
		Name = "光铳队长",
		DescTitle = "执勤规章8",
		DescText = "<Text_3_W>第八条：不要让你的部下在战区向你敬礼，这可能会导致敌人对你集中火力。</>",
	},
	[10046] = 
	{
		ID = 10046,
		MonsterID = 8,
		Name = "光铳队长",
		DescTitle = "善见笑话大全8",
		DescText = "<Text_3_W>据说有一位光铳队长是这样晋升的：某年某月某日，善见城里突然出现了一个自称「预言之子」的人，他说自己「不会被刀剑和子弹所伤害」，白刀队们对他无可奈何，很多人将他当成真的神子看待。这时一个光铳队员站出来一枪打死了他，因为「光铳队员的枪里没有子弹」，他也因此获得了晋升。</>",
	},
	[10047] = 
	{
		ID = 10047,
		MonsterID = 8,
		Name = "光铳队长",
		DescTitle = "赛博作战手册8",
		DescText = "<Text_3_W>任何时候都不要尝试直面光铳队长的射击，也不要相信</><Text_3_T>「用镜子可以反射粒子束武器」</><Text_3_W>的谣言，这一理论的发明者已经为此付出了惨痛的代价。</>",
	},
	[10048] = 
	{
		ID = 10048,
		MonsterID = 9,
		Name = "必安集团剑客",
		DescTitle = "前锋部队",
		DescText = "<Text_3_W>由「荒野」带队的雇佣部队，成员来源鱼龙混杂，但无一不是</><Text_3_T>街头斗殴的好手</><Text_3_W>。</>",
		FileImg = "T_GYB_02",
	},
	[10049] = 
	{
		ID = 10049,
		MonsterID = 9,
		Name = "必安集团剑客",
		DescTitle = "影子军队",
		DescText = "<Text_3_W>必安集团是一个善见城</><Text_3_T>准军事组织</><Text_3_W>，提供各类私人军事服务，由与天人议会关系密切的食品业巨头朴必安创立。</>",
		FileImg = "T_GYB_02",
	},
	[10050] = 
	{
		ID = 10050,
		MonsterID = 9,
		Name = "必安集团剑客",
		DescTitle = "第一滴血",
		DescText = "<Text_3_W>在善见城的角落仍然有天人议会的影响，必安集团就是它们的触角。在</><Text_3_T>白刀队「不适合」出现的场合</><Text_3_W>，必安集团的剑客会出手。</>",
		FileImg = "T_GYB_02",
	},
	[10051] = 
	{
		ID = 10051,
		MonsterID = 9,
		Name = "必安集团剑客",
		DescTitle = "行动规章1",
		DescText = "<Text_3_W>第一条：在执行任务中，务必穿戴整齐必安集团制服和各类配饰，要求衣帽整齐、鞋靴明亮，牢记</><Text_3_T>个人形象也代表着公司形象</><Text_3_W>。</>",
		FileImg = "T_GYB_02",
	},
	[10052] = 
	{
		ID = 10052,
		MonsterID = 9,
		Name = "必安集团剑客",
		DescTitle = "善见笑话大全9",
		DescText = "<Text_3_W>天人议会正在开会批评必安雇佣兵在赛博空间的行动迟缓，本应三个月净化完毕的四号扇区至今仍然眷族肆虐。开会途中，朴必安打来视频电话说：</>\n<Text_3_W>「我们刚刚清理了四号扇区的三号节点，这是一个伟大的胜利。」</>\n<Text_3_W>天人议会更加愤怒了，质问道：</>\n<Text_3_W>「那么剩下的一千零二十一个节点什么时候能够清理完？」</>\n<Text_3_W>「尊敬的阁下们，」视频里的朴必安耸耸肩，「您知道的，伟大的胜利并不常见。」</>",
		FileImg = "T_GYB_02",
	},
	[10053] = 
	{
		ID = 10053,
		MonsterID = 9,
		Name = "必安集团剑客",
		DescTitle = "赛博作战手册9",
		DescText = "<Text_3_W>千万不要将必安集团的剑客与天选组那些二流相提并论，他们凶狠、冷酷、不留余情，这是除了战斗技巧之外第二件我们需要向他们学习的事情——不是必须的，但</><Text_3_T>总得有人把手弄脏</><Text_3_W>。</>",
		FileImg = "T_GYB_02",
	},
	[10054] = 
	{
		ID = 10054,
		MonsterID = 10,
		Name = "必安集团力士",
		DescTitle = "中坚部队",
		DescText = "<Text_3_W>由「骑兵」带队的雇佣部队，以强壮的</><Text_3_T>囚犯兵</><Text_3_W>为中坚力量。</>",
		FileImg = "T_GYB_03",
	},
	[10055] = 
	{
		ID = 10055,
		MonsterID = 10,
		Name = "必安集团力士",
		DescTitle = "风险投资",
		DescText = "<Text_3_W>通过在善见城重刑监狱中布置非公开的招募点，必安集团获得了十分「优质」的兵员地，朴必安深知这些人身上包含的巨大风险，</><Text_3_T>但潜在收益仍然激励集团继续招募这些暴徒</><Text_3_W>。</>",
		FileImg = "T_GYB_03",
	},
	[10056] = 
	{
		ID = 10056,
		MonsterID = 10,
		Name = "必安集团力士",
		DescTitle = "势不可挡",
		DescText = "<Text_3_W>对于这些大力士来说，耍弄沉重的斧钺并不困难，这使得他们的攻击往往是漫不经心的——</><Text_3_T>巨大的非必要伤害会令他们更加卖力</><Text_3_W>。</>",
		FileImg = "T_GYB_03",
	},
	[10057] = 
	{
		ID = 10057,
		MonsterID = 10,
		Name = "必安集团力士",
		DescTitle = "行动规章2",
		DescText = "<Text_3_W>第二条：与天选组武装不同，你们不需要顾及舆论和所谓「人道主义」的掣肘，我们只需要你们做你们最擅长的事：</><Text_3_T>散布恐惧，使用暴力，大肆破坏</><Text_3_W>。</>",
		FileImg = "T_GYB_03",
	},
	[10058] = 
	{
		ID = 10058,
		MonsterID = 10,
		Name = "必安集团力士",
		DescTitle = "善见笑话大全10",
		DescText = "<Text_3_W>一个路人问一名必安集团力士：「我听说你曾经多次在白噪里面同眷族战斗，那是什么样的体验？」</>\n<Text_3_W>「非常恐怖，就像地狱一样，没有几个比那里更可怕的地方了。」</>\n<Text_3_W>路人又问：「既然这么恐怖，那你为什么还要去呢？」</>\n<Text_3_W>「开什么玩笑，」力士瞪大了双眼，「你要我回善见城监狱吗？」</>",
		FileImg = "T_GYB_03",
	},
	[10059] = 
	{
		ID = 10059,
		MonsterID = 10,
		Name = "必安集团力士",
		DescTitle = "赛博作战手册10",
		DescText = "<Text_3_W>与天选组破障队相比，力士的攻击欲望更加强烈且凶恶，在善见城最危险、混乱的地方学到这些实属正常，但这也导致他们很容易</><Text_3_T>被肾上腺素冲昏头脑</><Text_3_W>，这就是我们逃跑或者将他们打倒的机会。</>",
		FileImg = "T_GYB_03",
	},
	[10060] = 
	{
		ID = 10060,
		MonsterID = 11,
		Name = "必安集团炮手",
		DescTitle = "主力部队",
		DescText = "<Text_3_W>由「法师」带队的雇佣部队，使用</><Text_3_T>杀伤范围极大的抛射榴弹</><Text_3_W>作为武器，破坏力惊人。</>",
		FileImg = "T_GYB_01",
	},
	[10061] = 
	{
		ID = 10061,
		MonsterID = 11,
		Name = "必安集团炮手",
		DescTitle = "斗殴之王",
		DescText = "<Text_3_W>必安集团佣兵的标志是它的近战部队，但其真正的战斗核心则是炮手部队。在近战单位牵制住对手后，</><Text_3_T>炮手的榴弹会在双方的接触线上爆炸</><Text_3_W>。</>",
		FileImg = "T_GYB_01",
	},
	[10062] = 
	{
		ID = 10062,
		MonsterID = 11,
		Name = "必安集团炮手",
		DescTitle = "完全友伤",
		DescText = "<Text_3_W>毫无疑问，必安集团炮兵的作战方式会</><Text_3_T>对队友造成巨大的伤害</><Text_3_W>，但剑客和力士们并无需多怨言，这种风险体现在了他们的工资里。</>",
		FileImg = "T_GYB_01",
	},
	[10063] = 
	{
		ID = 10063,
		MonsterID = 11,
		Name = "必安集团炮手",
		DescTitle = "行动规章3",
		DescText = "<Text_3_W>第三条：你们是必安武装火力的中坚，你们在任何情况下均拥有</><Text_3_T>完全的火力调用权限</><Text_3_W>。但是请记住，你们打出去的每一发榴弹都价值300个素食热狗。为了公司，也为了你们自己的节约奖金，务必节省弹药！</>",
		FileImg = "T_GYB_01",
	},
	[10064] = 
	{
		ID = 10064,
		MonsterID = 11,
		Name = "必安集团炮手",
		DescTitle = "善见笑话大全11",
		DescText = "<Text_3_W>年会上，朴必安在台上大吹大擂上一财年降本增效的成果，台下一个炮手喊道：「我不想听你讲这些没用的，我只想知道必安集团的弹药去哪里了。」</>\n<Text_3_W>第二天，朴必安继续在台上大吹大擂，台下的剑客怯生生地举手问道：「我不想知道必安集团的弹药去哪里了，我只想知道炮手去哪里了。」</>",
		FileImg = "T_GYB_01",
	},
	[10065] = 
	{
		ID = 10065,
		MonsterID = 11,
		Name = "必安集团炮手",
		DescTitle = "赛博作战手册11",
		DescText = "<Text_3_W>必安炮手是久负盛名的火力支援角色，他们追求精准的预判与恰到好处的火力，对效益最大化的追求令他们成为难缠的对手。</><Text_3_T>频繁无规则的机动可以有效影响炮手的预瞄</><Text_3_W>，但还是优先将他们解决为妙，以绝后患。</>",
		FileImg = "T_GYB_01",
	},
	[10066] = 
	{
		ID = 10066,
		MonsterID = 12,
		Name = "必安集团枪手",
		DescTitle = "执行部队",
		DescText = "<Text_3_W>由「阴影」带队的射击兵部队，他们会向面前的</><Text_3_T>一切</><Text_3_W>开火。</>",
		FileImg = "T_GYB_04",
	},
	[10067] = 
	{
		ID = 10067,
		MonsterID = 12,
		Name = "必安集团枪手",
		DescTitle = "注意避让",
		DescText = "<Text_3_W>必安集团雇佣的枪手都是一流的猎人，他们对战友非常温柔，会在开枪前尽到提醒的义务——提醒等于</><Text_3_T>免责</><Text_3_W>。</>",
		FileImg = "T_GYB_04",
	},
	[10068] = 
	{
		ID = 10068,
		MonsterID = 12,
		Name = "必安集团枪手",
		DescTitle = "无限开火",
		DescText = "<Text_3_W>枪手部队的目标不仅有对面的敌人，也包括</><Text_3_T>潜在的逃兵与失控可能大于80%的力士单位</><Text_3_W>。</>",
		FileImg = "T_GYB_04",
	},
	[10069] = 
	{
		ID = 10069,
		MonsterID = 12,
		Name = "必安集团枪手",
		DescTitle = "行动规章4",
		DescText = "<Text_3_W>第五条：作为必安集团的底牌，你们拥有</><Text_3_T>第五裁量权</><Text_3_W>，即在任何必要的时候，清除</><Text_3_T>任何对必安集团利益造成威胁的个人与团体</><Text_3_W>。目标</><Text_3_T>不分敌我，不问人畜，不需获取上级批准</><Text_3_W>。</>\n<Text_3_W>本条为隐藏条款，请务必对其他兵种成员和外界保密。泄密者将被</><Text_3_T>抹除</><Text_3_W>。</>\n<Text_3_W>——总裁朴必安</>",
		FileImg = "T_GYB_04",
	},
	[10070] = 
	{
		ID = 10070,
		MonsterID = 12,
		Name = "必安集团枪手",
		DescTitle = "善见笑话大全12",
		DescText = "<Text_3_W>第六扇区即将发生白噪，即将进入宵禁状态，两个必安枪手正在巡逻。这时，一个人在他们前面跑过，一名枪手马上抬手打了他一枪。</>\n<Text_3_W>「你疯了吗？为什么要打他，你认识他吗？」</>\n<Text_3_W>「他是我的邻居。」</>\n<Text_3_W>「现在还没有宵禁，你为什么要这么做？」</>\n<Text_3_W>「我知道他住哪，宵禁令开始前他肯定到不了家了。」</>",
		FileImg = "T_GYB_04",
	},
	[10071] = 
	{
		ID = 10071,
		MonsterID = 12,
		Name = "必安集团枪手",
		DescTitle = "赛博作战手册12",
		DescText = "<Text_3_W>沉稳、精准、无情，你已经领教过必安枪手们的「射击艺术」了。我们并没有更多的建议，都是些老生常谈：你需要快速移动，时刻注意红色激光的提醒，尽快击倒不擅近战的他们，以及最重要的——你需要一点</><Text_3_T>好运气</><Text_3_W>。</>",
		FileImg = "T_GYB_04",
	},
	[10072] = 
	{
		ID = 10072,
		MonsterID = 13,
		Name = "剑友信士",
		DescTitle = "赐福",
		DescText = "<Text_3_W>祂的光辉无弗远届，永远照耀着我们，</>\n<Text_3_W>祂褒扬我们的信任，祝福我们的宝剑，</>\n<Text_3_W>我们敲响剑刃，</>\n<Text_3_T>用金石之音歌颂您的恩赏。</>",
		FileImg = "T_CMJT_02",
	},
	[10073] = 
	{
		ID = 10073,
		MonsterID = 13,
		Name = "剑友信士",
		DescTitle = "怜悯",
		DescText = "<Text_3_W>我们怜悯刀下的敌人，如同祂怜悯无知的我们，</>\n<Text_3_T>我们信赖刀刃的锋利，如同祂信任忠诚的我们。</>",
		FileImg = "T_CMJT_02",
	},
	[10074] = 
	{
		ID = 10074,
		MonsterID = 13,
		Name = "剑友信士",
		DescTitle = "降祸",
		DescText = "<Text_3_W>在那应到之日，</>\n<Text_3_T>善见城将烧作灰烬，</>\n<Text_3_W>如同祂流传的预言，</>\n<Text_3_T>我们是持刀的审判者，</>\n<Text_3_W>公正地裁决一切，</>\n<Text_3_T>在那应到之日。</>",
		FileImg = "T_CMJT_02",
	},
	[10075] = 
	{
		ID = 10075,
		MonsterID = 13,
		Name = "剑友信士",
		DescTitle = "布道书1",
		DescText = "<Text_3_W>刀刃锋利，需要每日磨砺；技巧娴熟，需要每日练习；而明心见性，需要每日祈祷。</>\n<Text_3_T>等待绝非徒劳，时日将近，做好准备。</>",
		FileImg = "T_CMJT_02",
	},
	[10076] = 
	{
		ID = 10076,
		MonsterID = 13,
		Name = "剑友信士",
		DescTitle = "善见未解之谜1",
		DescText = "<Text_3_W>目击报告：零类接触，数个在白噪中看到人形生物的案例。天人议会强调这是因为他们「看错了」，但各种猜测仍然在坊间流传。最流行的看法是眷族之中衍生出了</><Text_3_T>拟人</><Text_3_W>的品种，它们已经混入我们社会伺机作乱。这种看法对了一半。</>",
		FileImg = "T_CMJT_02",
	},
	[10077] = 
	{
		ID = 10077,
		MonsterID = 13,
		Name = "剑友信士",
		DescTitle = "赛博作战手册13",
		DescText = "<Text_3_W>与白刀队不同，这些虔诚信徒的攻击欲望并不强烈，他们似乎将剑术视做</><Text_3_T>某种修行</><Text_3_W>而非伤害他人的方法。如果没有必要，不必与他们交战。但如果已避无可避，务必小心，剑友的剑法优雅而致命，决不可掉以轻心。</>",
		FileImg = "T_CMJT_02",
	},
	[10078] = 
	{
		ID = 10078,
		MonsterID = 14,
		Name = "力友信士",
		DescTitle = "鸣笛",
		DescText = "<Text_3_W>祂的笛声穿过虚妄的原野，</>\n<Text_3_W>穿越常人的躯壳，</>\n<Text_3_W>赐予我们强健的筋骨，</>\n<Text_3_T>我们感念祂的赐福，捍卫祂的荣宠。</>",
		FileImg = "T_CMJT_03",
	},
	[10079] = 
	{
		ID = 10079,
		MonsterID = 14,
		Name = "力友信士",
		DescTitle = "仁慈",
		DescText = "<Text_3_W>祂温柔的光辉教导我们去拯救，</>\n<Text_3_W>祂慈爱的言语命令我们去传道，</>\n<Text_3_W>低下头，</>\n<Text_3_T>我将为你们带来仁慈。</>",
		FileImg = "T_CMJT_03",
	},
	[10080] = 
	{
		ID = 10080,
		MonsterID = 14,
		Name = "力友信士",
		DescTitle = "降祸",
		DescText = "<Text_3_W>在那应到之日，</>\n<Text_3_T>善见城将烧作灰烬，</>\n<Text_3_W>如同祂流传的预言，</>\n<Text_3_T>我们是持斧的行刑者，</>\n<Text_3_W>按律法执行应得的刑罚，</>\n<Text_3_T>在那应到之日。</>",
		FileImg = "T_CMJT_03",
	},
	[10081] = 
	{
		ID = 10081,
		MonsterID = 14,
		Name = "力友信士",
		DescTitle = "布道书2",
		DescText = "<Text_3_W>布置陷阱的猎人，早晚被陷阱伤害；污损城垣的，毒蛇将会跟着他。徒有力量而不念神恩，斧子会在使用时偏移。</>\n<Text_3_T>等待绝非徒劳，时日将近，做好准备。</>",
		FileImg = "T_CMJT_03",
	},
	[10082] = 
	{
		ID = 10082,
		MonsterID = 14,
		Name = "力友信士",
		DescTitle = "善见未解之谜2",
		DescText = "<Text_3_W>目击报告：第一类接触，在白噪中遭遇眷族时被人形生物搭救的案例。天人议会将此类事件宣传为天选组干员舍身救险的事迹，但据当事人描述，该人型生物</><Text_3_T>披挂宽阔的斗篷</><Text_3_W>，且力大无比，不似天选组作风。</>",
		FileImg = "T_CMJT_03",
	},
	[10083] = 
	{
		ID = 10083,
		MonsterID = 14,
		Name = "力友信士",
		DescTitle = "赛博作战手册14",
		DescText = "<Text_3_W>很难想象他们并不魁梧的身形竟蕴含着如此力量，他们挥舞斧子的步伐严格依照某种</><Text_3_T>仪轨</><Text_3_W>，寻找其中规律，尽量避开他们的强力攻击，知易行难。</>",
		FileImg = "T_CMJT_03",
	},
	[10084] = 
	{
		ID = 10084,
		MonsterID = 15,
		Name = "掷弹信士",
		DescTitle = "颂唱",
		DescText = "<Text_3_W>我们本应同常人化作灰烬，</>\n<Text_3_W>祂帮助了我们，</>\n<Text_3_W>我们蒙祂的恩宠，领受祂的火焰，</>\n<Text_3_T>我们为祂将地土点亮。</>",
		FileImg = "T_CMJT_01",
	},
	[10085] = 
	{
		ID = 10085,
		MonsterID = 15,
		Name = "掷弹信士",
		DescTitle = "净化",
		DescText = "<Text_3_W>火焰是必要的考验，</>\n<Text_3_W>火焰是净化的歌声，</>\n<Text_3_T>祂的世界以火焰净化，</>\n<Text_3_W>我们是祂的代行。</>",
		FileImg = "T_CMJT_01",
	},
	[10086] = 
	{
		ID = 10086,
		MonsterID = 15,
		Name = "掷弹信士",
		DescTitle = "降祸",
		DescText = "<Text_3_W>在那应到之日，</>\n<Text_3_T>善见城将烧作灰烬，</>\n<Text_3_W>如同祂流传的预言，</>\n<Text_3_T>我们是闪烁的迎宾人，</>\n<Text_3_W>光芒与火花点燃天空，</>\n<Text_3_T>在那应到之日。</>",
		FileImg = "T_CMJT_01",
	},
	[10087] = 
	{
		ID = 10087,
		MonsterID = 15,
		Name = "掷弹信士",
		DescTitle = "布道书3",
		DescText = "<Text_3_W>火焰神圣，昭明天下；罪恶污秽，无所遁形。火焰在手，永世不灭；铺陈鎏金，净化世界。</>\n<Text_3_T>等待绝非徒劳，时日将近，做好准备。</>",
		FileImg = "T_CMJT_01",
	},
	[10088] = 
	{
		ID = 10088,
		MonsterID = 15,
		Name = "掷弹信士",
		DescTitle = "善见未解之谜3",
		DescText = "<Text_3_W>目击报告：零类接触，数个看到红色白噪的案例。天人议会警告这是高级眷族出没的信号，要求市民马上躲避。但根据目击报告显示，红色白噪出现后不久白噪天气便消散，一些猜测认为这是某些势力正在进行</><Text_3_T>驱雾仪式</><Text_3_W>。</>",
		FileImg = "T_CMJT_01",
	},
	[10089] = 
	{
		ID = 10089,
		MonsterID = 15,
		Name = "掷弹信士",
		DescTitle = "赛博作战手册15",
		DescText = "<Text_3_W>一些赛博空间冒险者表示在与掷弹信士交战时曾听到某种</><Text_3_T>吟诵声音</><Text_3_W>，注意力分散导致被爆炸击中，这可能是信士作战的一种特别技能，应当引起注意，并采取手段规避。（怎么在赛博空间塞住耳朵是个问题——批注）</>",
		FileImg = "T_CMJT_01",
	},
	[10090] = 
	{
		ID = 10090,
		MonsterID = 16,
		Name = "枪械信士",
		DescTitle = "拭泪",
		DescText = "<Text_3_W>在那泪水充盈之日，</>\n<Text_3_W>祂怜惜我们，擦亮了我们的眼睛，</>\n<Text_3_W>把祂的枪赐予我们，</>\n<Text_3_T>从此，我们不再流泪。</>",
		FileImg = "T_CMJT_04",
	},
	[10091] = 
	{
		ID = 10091,
		MonsterID = 16,
		Name = "枪械信士",
		DescTitle = "明辨",
		DescText = "<Text_3_W>祂令我们眼睛明亮，</>\n<Text_3_W>隐藏的都已显现，</>\n<Text_3_W>我们回报祂的恩赏，</>\n<Text_3_T>让祂的裁判显现。</>",
		FileImg = "T_CMJT_04",
	},
	[10092] = 
	{
		ID = 10092,
		MonsterID = 16,
		Name = "枪械信士",
		DescTitle = "降祸",
		DescText = "<Text_3_W>在那应到之日，</>\n<Text_3_T>善见城将烧作灰烬，</>\n<Text_3_W>如同祂流传的预言，</>\n<Text_3_T>我们是傲立的禁卫军，</>\n<Text_3_W>我们的行列开辟祂降临的足迹，</>\n<Text_3_T>在那应到之日。</>",
		FileImg = "T_CMJT_04",
	},
	[10093] = 
	{
		ID = 10093,
		MonsterID = 16,
		Name = "枪械信士",
		DescTitle = "布道书4",
		DescText = "<Text_3_W>心眼合一，后发而先至；明台澄净，正射而必中。</>\n<Text_3_T>等待绝非徒劳，时日将近，做好准备。</>",
		FileImg = "T_CMJT_04",
	},
	[10094] = 
	{
		ID = 10094,
		MonsterID = 16,
		Name = "枪械信士",
		DescTitle = "善见未解之谜4",
		DescText = "<Text_3_W>目击报告：第一类接触，在白噪中遭遇眷族时被雾中射出的子弹搭救的案例。天人议会将此类事件宣传为天选组干员的义举。但根据目击报告显示，</><Text_3_T>武器射流的颜色与天选组使用武器并不相同</><Text_3_W>。很难相信善见城内还有另一支不知名的武装，这确实令人恐慌。</>",
		FileImg = "T_CMJT_04",
	},
	[10095] = 
	{
		ID = 10095,
		MonsterID = 16,
		Name = "枪械信士",
		DescTitle = "赛博作战手册16",
		DescText = "<Text_3_W>枪械信士相信自己的武器收到了祝福，其精准度大有提升。诡异的是，</><Text_3_T>赛博空间探险者们在某种程度上似乎也相信这一点</><Text_3_W>，可能是因为信士们卓越的射击技巧。</>",
		FileImg = "T_CMJT_04",
	},
	[10096] = 
	{
		ID = 10096,
		MonsterID = 22,
		Name = "末法龙王",
		DescTitle = "苏生",
		DescText = "<Text_3_W>当代码重新归于永恒之河时，</>\n<Text_3_W>当规则在数据流里销毁之时，</>\n<Text_3_T>龙之阴影，从黑暗的湍流中苏生。</>",
		FileImg = "T_MFLW",
	},
	[10097] = 
	{
		ID = 10097,
		MonsterID = 22,
		Name = "末法龙王",
		DescTitle = "卸甲",
		DescText = "<Text_3_W>龙角断折，如</><Text_3_T>尘归尘</><Text_3_W>，</>\n<Text_3_W>龙麟褪尽，如</><Text_3_T>土归土</><Text_3_W>。</>",
		FileImg = "T_MFLW",
	},
	[10098] = 
	{
		ID = 10098,
		MonsterID = 22,
		Name = "末法龙王",
		DescTitle = "归途",
		DescText = "<Text_3_W>往日之谜归于之河，</>\n<Text_3_W>于母神的微笑中封存</><Text_3_T>旧日的荣光</><Text_3_W>。</>",
		FileImg = "T_MFLW",
	},
	[10099] = 
	{
		ID = 10099,
		MonsterID = 22,
		Name = "末法龙王",
		DescTitle = "眷族观察手记1",
		DescText = "<Text_3_W>个体呈龙型，机械质感，有四只类似人类的手臂，身体佝偻，脖子弯曲，有疑似脊椎骨骼向外凸出。</>\n<Text_3_W>龙身附着多个人脸结构，作用尚不明确。有手持兵器，类似薙刀。</>\n<Text_3_W>威胁等级：</><Text_3_T>极高</>",
		FileImg = "T_MFLW",
	},
	[10100] = 
	{
		ID = 10100,
		MonsterID = 22,
		Name = "末法龙王",
		DescTitle = "善见未解之谜5",
		DescText = "<Text_3_W>目击报告：第三类接触，天选组干员被白噪中的巨大生物个体杀死的案例，过程被记录仪拍下。视频原件已被天人议会封存，一些流出的片段展示了干员被巨大生物用残忍方式杀死的恐怖场景，论坛中出现了将之与传说中的</><Text_3_T>龙</><Text_3_W>相提并论的讨论串，被批为无稽之谈。</>",
		FileImg = "T_MFLW",
	},
	[10101] = 
	{
		ID = 10101,
		MonsterID = 22,
		Name = "末法龙王",
		DescTitle = "赛博作战手册17",
		DescText = "<Text_3_W>出于最起码的良知，我不会建议你与这种生物交战，这与其说是考验不如说是自杀。如果你坚持的话，请利用好这种生物与生俱来的自负，它很喜欢向你展示各种攻击手段，而它</><Text_3_T>切换时的间隙</><Text_3_W>就是你杀伤的机会。</>",
		FileImg = "T_MFLW",
	},
	[10102] = 
	{
		ID = 10102,
		MonsterID = 24,
		Name = "青儿",
		DescTitle = "糖河",
		DescText = "<Text_3_W>孤儿院里的卫兵，</>\n<Text_3_W>吃着糖，</>\n<Text_3_W>因为甜味儿高兴，</>\n<Text_3_T>她是你的女儿和姐妹。</>",
		FileImg = "T_QE_01",
	},
	[10103] = 
	{
		ID = 10103,
		MonsterID = 24,
		Name = "青儿",
		DescTitle = "蛇往何处爬",
		DescText = "<Text_3_W>众人陷入沉睡，</>\n<Text_3_W>夜色支离破碎，</>\n<Text_3_W>实验室大楼上方，</>\n<Text_3_T>灰烬和鲜血飞溅。</>",
		FileImg = "T_QE_01",
	},
	[10104] = 
	{
		ID = 10104,
		MonsterID = 24,
		Name = "青儿",
		DescTitle = "苹果园",
		DescText = "<Text_3_T>我没来过此处，</>\n<Text_3_T>终点在哪里？尽头在哪里？有谁看见了？</>\n<Text_3_T>而你此刻是谁？你是谁？</>",
		FileImg = "T_QE_01",
	},
	[10105] = 
	{
		ID = 10105,
		MonsterID = 24,
		Name = "青儿",
		DescTitle = "侦探记事本1",
		DescText = "<Text_3_W>优雅，善变，真假莫辨，有着令人难忘的金色蛇瞳，习惯居高临下地斜眼看人。</>\n<Text_3_W>战斗服呈现暗青色皮质材质，材料不明，似乎与身上刺青有功能上的关联。</>\n<Text_3_T>十分危险，也魅力非凡。</>",
		FileImg = "T_QE_01",
	},
	[10106] = 
	{
		ID = 10106,
		MonsterID = 24,
		Name = "青儿",
		DescTitle = "侦探记事本2",
		DescText = "<Text_3_W>作为白真真的反面，具有极为强大的行动力，爱憎分明，言未必信但行必果。</>\n<Text_3_W>对白真真的情愫很难用友情、亲情乃至爱情概括，这是一种更加复杂且隐秘的关联，说不清道不明，但是紧紧相连，未曾分开过。任何企图动摇这种关联的行为都会招致</><Text_3_T>严厉的报复</><Text_3_W>。</>",
		FileImg = "T_QE_01",
	},
	[10107] = 
	{
		ID = 10107,
		MonsterID = 24,
		Name = "青儿",
		DescTitle = "青儿的留言",
		DescText = "<Text_3_W>大侦探，对我手下留情了吗？我好感动呀。不过，我还是更喜欢认真的人哦，下次约会时要记得~</>",
		FileImg = "T_QE_01",
	},
	[10108] = 
	{
		ID = 10108,
		MonsterID = 25,
		Name = "不死丸",
		DescTitle = "光荣近卫",
		DescText = "<Text_3_W>永远鲜明帝国之拱卫，永生不死的武士，光荣的</><Text_3_T>近卫之花</><Text_3_W>，它有很多名字，你应当敬畏。</>",
		FileImg = "T_BSW_01",
	},
	[10109] = 
	{
		ID = 10109,
		MonsterID = 25,
		Name = "不死丸",
		DescTitle = "百炼精兵",
		DescText = "<Text_3_W>刺破天机之竹取长枪，千锤百炼之精甲重盾，劈开长云之方正战斧，炸碎群星之阳电子炮，这是</><Text_3_T>帝国的兵器</><Text_3_W>，这是它的兵器，你应当敬畏。</>",
		FileImg = "T_BSW_01",
	},
	[10110] = 
	{
		ID = 10110,
		MonsterID = 25,
		Name = "不死丸",
		DescTitle = "辱没结局",
		DescText = "<Text_3_W>你不应敬畏，因为如此伟力仍然无法令帝国重光，</>\n<Text_3_W>你应当敬畏，因为覆灭了帝国的伟力仍</><Text_3_T>不能污损它的荣耀</><Text_3_W>。</>",
		FileImg = "T_BSW_01",
	},
	[10111] = 
	{
		ID = 10111,
		MonsterID = 25,
		Name = "不死丸",
		DescTitle = "侦探记事本3",
		DescText = "<Text_3_W>不愧是帝国近卫最璀璨的明星，数十年后，他的武艺仍然精妙绝伦，甚至比那悲剧一日时尚未垂朽的自己更加华丽。</>\n<Text_3_T>刀剑易折，人心难移。</><Text_3_W>这是他事迹的发端，也是他苦难的源泉。</>",
		FileImg = "T_BSW_01",
	},
	[10112] = 
	{
		ID = 10112,
		MonsterID = 25,
		Name = "不死丸",
		DescTitle = "侦探记事本4",
		DescText = "<Text_3_W>很难在我们的时代再见到如此老派的爱国者：付出一切、战斗到底，然后不出所料地被「背叛」，连带那份忠勇也化作刺向自己的刀刃。</>\n<Text_3_W>可惜时间并没有慈悲地将苦难用遗忘包裹，在白噪的影响下，</><Text_3_T>那份痛苦愈发锋利可怖</><Text_3_W>。</>",
		FileImg = "T_BSW_01",
	},
	[10113] = 
	{
		ID = 10113,
		MonsterID = 25,
		Name = "不死丸",
		DescTitle = "不死丸的留言",
		DescText = "<Text_3_W>年轻人，我没有冒犯你的意思，但你真的认为这样放水我会看不出吗？我不需要这样的「敬老」，我需要你付出百分之一百二十的努力打败我，那样我才能感受到你的尊重。</>",
		FileImg = "T_BSW_01",
	},
	[10114] = 
	{
		ID = 10114,
		MonsterID = 26,
		Name = "突击监兵",
		DescTitle = "坚守战线",
		DescText = "<Text_3_W>天选组武装的骄傲，由</><Text_3_T>奥秘科技</><Text_3_W>推出的恩德-209型模块化步战平台近距离作战型机甲组成，是善见城防面对大规模威胁时坚不可摧的钢铁城墙。</>",
		FileImg = "T_JB_01",
	},
	[10115] = 
	{
		ID = 10115,
		MonsterID = 26,
		Name = "突击监兵",
		DescTitle = "马上后退",
		DescText = "<Text_3_W>作为天选组装甲部队的前锋，突击监兵装甲厚重，装备有</><Text_3_T>偏转力场护盾和动粒子矛</><Text_3_W>，基本不存在能够与之正面对抗的个体。</>",
		FileImg = "T_JB_01",
	},
	[10116] = 
	{
		ID = 10116,
		MonsterID = 26,
		Name = "突击监兵",
		DescTitle = "二次创作",
		DescText = "<Text_3_W>尽管奥秘科技声称恩德-209型步战平台完全基于自身技术积累研发，但根据一些来源不明的信息碎片显示，这种机甲是以高墙之外的</><Text_3_T>大型眷族</><Text_3_W>为蓝本开发的。两者相似度几何尚未可知。</>",
		FileImg = "T_JB_01",
	},
	[10117] = 
	{
		ID = 10117,
		MonsterID = 26,
		Name = "突击监兵",
		DescTitle = "机甲知识1",
		DescText = "<Text_3_W>监兵机甲的创造者奥秘科技是久负盛名的日用工业品制造公司——是的，它是善见城最大的白色家电制造商，这种</><Text_3_T>技术方向与最终产品的完全错位</><Text_3_W>也是监兵系列机甲一经问世就引发了各类阴谋论的根本原因。</>",
		FileImg = "T_JB_01",
	},
	[10118] = 
	{
		ID = 10118,
		MonsterID = 26,
		Name = "突击监兵",
		DescTitle = "密级开发文档1",
		DescText = "<Text_3_W>「杨先生，现在我们为你展示恩德试验机的执法功能。不用害怕，它完全受控。请你拿好这把枪，对准机甲。」</>\n<Text_3_W>「你看，它可以识别你手中的武器，现在按照它的指令放下武器。」</>\n<Text_3_W>「恩德？他已经解除武装，停止执法！恩德，停机！」</>\n<Text_3_W>「（枪声，尖叫声，家具爆裂声）」</>",
		FileImg = "T_JB_01",
	},
	[10119] = 
	{
		ID = 10119,
		MonsterID = 26,
		Name = "突击监兵",
		DescTitle = "赛博作战手册20",
		DescText = "<Text_3_W>突击监兵是兼顾防御与灵活的高机动单位，不要尝试挡在它的冲锋路线上，</><Text_3_T>尝试它在原地短暂停留时给予它伤害</><Text_3_W>。与突击监兵兵刃相交极其危险，但不是不可行，这带来的冲击</><Text_3_T>可能对其机体造成短暂的过载</><Text_3_W>，这将给你对它造成高额伤害的机会。</>",
		FileImg = "T_JB_01",
	},
	[10120] = 
	{
		ID = 10120,
		MonsterID = 27,
		Name = "强袭监兵",
		DescTitle = "开路先锋",
		DescText = "<Text_3_W>由奥秘科技推出的恩德-209型模块化步战平台近距离作战型机甲改型，格外强化了</><Text_3_T>上肢的结构强度与发力单元</><Text_3_W>，使其可以挥动极为沉重的大斧进行攻击。</>",
		FileImg = "T_JB_02",
	},
	[10121] = 
	{
		ID = 10121,
		MonsterID = 27,
		Name = "强袭监兵",
		DescTitle = "无可匹敌",
		DescText = "<Text_3_W>强袭监兵的目标是谁？目前看来，无论是一般的破坏分子还是偶尔渗透进来的小型眷族都不是它的对手，天人议会为何要装备这种</><Text_3_T>昂贵的溢出武力</><Text_3_W>？</>",
		FileImg = "T_JB_02",
	},
	[10122] = 
	{
		ID = 10122,
		MonsterID = 27,
		Name = "强袭监兵",
		DescTitle = "残酷的心",
		DescText = "<Text_3_W>与突击监兵完全由AI控制不同，强袭监兵由人类驾驶员远程控制，据说是因为</><Text_3_T>「该单位的战斗行为需要格外的残忍和仇恨，AI认为这是不可理解的，这会限制强袭监兵的战斗发挥」</><Text_3_W>。</>",
		FileImg = "T_JB_02",
	},
	[10123] = 
	{
		ID = 10123,
		MonsterID = 27,
		Name = "强袭监兵",
		DescTitle = "机甲知识2",
		DescText = "<Text_3_W>在奥秘科技放出的监兵机甲设计初稿中可以看到，监兵机甲早期试验机还是一个用光滑的银色圆形外壳包裹身体的「某种东西」，看起来完全不具备战斗力，就像一个「会走路的冷压榨汁机」（赛博论坛评论）。至于为何它会从榨汁机变成今天模样，恐怕要等奥秘科技自己解答了。</>",
		FileImg = "T_JB_02",
	},
	[10124] = 
	{
		ID = 10124,
		MonsterID = 27,
		Name = "强袭监兵",
		DescTitle = "密级开发文档2",
		DescText = "<Text_3_W>「所以我们不会再使用自研的AI架构？」</>\n<Text_3_W>「仍然使用，先生，但是需要借助一些其他的…东西。」</>\n<Text_3_W>「比如？」</>\n<Text_3_W>「比如这个。（掀开布料声）我们的研究员尝试将它的思维系统接入恩德的AI模型内，它出乎意料地顺利运行起来。我知道您担忧这其中的风险，但我可以保证，它完全受控。」</>",
		FileImg = "T_JB_02",
	},
	[10125] = 
	{
		ID = 10125,
		MonsterID = 27,
		Name = "强袭监兵",
		DescTitle = "赛博作战手册21",
		DescText = "<Text_3_W>强袭监兵相对突击型进一步强化了力量属性，若未能及时闪避将造成灾难性的后果。好在它为提供最大的力量输出</><Text_3_T>牺牲了部分防御设备</><Text_3_W>，这为我们寻找机会将它击倒提供了可能。不要贪图造成更多伤害而忘记及时撤退，这是一首容不得疏忽的华尔兹。</>",
		FileImg = "T_JB_02",
	},
	[10126] = 
	{
		ID = 10126,
		MonsterID = 28,
		Name = "枪炮监兵",
		DescTitle = "活火熔城",
		DescText = "<Text_3_W>由奥秘科技推出的恩德-209型模块化步战平台远程作战型机甲，装备</><Text_3_T>燃烧榴弹</><Text_3_W>，可以在短时间内将大片土地化作火海。</>",
		FileImg = "T_JB_03",
	},
	[10127] = 
	{
		ID = 10127,
		MonsterID = 28,
		Name = "枪炮监兵",
		DescTitle = "远烧近枪",
		DescText = "<Text_3_W>除了伤害面积颇大的燃烧榴弹，枪炮监兵还持有一把</><Text_3_T>全自动霰弹枪</><Text_3_W>，其弹丸速度与质量足以击穿轻型装甲目标，这种某种程度上比榴弹更可怕的武器被用来对付距离过近的敌方单位。</>",
		FileImg = "T_JB_03",
	},
	[10128] = 
	{
		ID = 10128,
		MonsterID = 28,
		Name = "枪炮监兵",
		DescTitle = "最后手段",
		DescText = "<Text_3_W>根据一位天人议会政府内部不具名人士的说法，枪炮监兵</><Text_3_T>并未安装敌我识别模块</><Text_3_W>，这意味着一旦解开开火保险，它面前的一切都会被判定为攻击目标，这是一种针对善见城内可能发生的最严重态势的</><Text_3_T>最终应对方案</><Text_3_W>。</>",
		FileImg = "T_JB_03",
	},
	[10129] = 
	{
		ID = 10129,
		MonsterID = 28,
		Name = "枪炮监兵",
		DescTitle = "机甲知识3",
		DescText = "<Text_3_W>有关监兵机甲安全性的讨论已经成为善见城上下的周常问题，尽管奥秘科技一再强调他们对所有监兵机甲具备完全的「控制性」，但其装备的极为强大的武力仍然为市民所诟病：</><Text_3_T>很难想象什么样的敌人需要用动粒子矛和燃烧榴弹来镇压，哪怕是在白噪里</><Text_3_W>。</>",
		FileImg = "T_JB_03",
	},
	[10130] = 
	{
		ID = 10130,
		MonsterID = 28,
		Name = "枪炮监兵",
		DescTitle = "密级开发文档3",
		DescText = "<Text_3_W>「我不在乎伦理问题，我只在乎这东西能不能拿到天选组的订单。把我们最好的武装全都加上去，要让所有人一旦看到恩德-209就再也移不开视线！」</>\n<Text_3_W>「市民不知道他们需要什么，天选组也不知道——我们知道，所以我们要教育他们，把最好的机甲交给他们，他们就会自己找到用途，就像拿到新玩具的孩子。」</>\n<Text_3_W>「从此，奥秘科技将</><Text_3_T>遥遥领先</><Text_3_W>。」</>",
		FileImg = "T_JB_03",
	},
	[10131] = 
	{
		ID = 10131,
		MonsterID = 28,
		Name = "枪炮监兵",
		DescTitle = "赛博作战手册22",
		DescText = "<Text_3_W>你将面对善见城最为强大的人造执法力量，你将很难全身而退，尽力在自己完全失去意识前打倒它。时刻注意它抛出榴弹的位置，躲避任何爆炸冲击，</><Text_3_T>在近身搏斗时警惕它切换近战模式</><Text_3_W>，你一定不想品尝它装备的霰弹弹丸的滋味。</>",
		FileImg = "T_JB_03",
	},
	[10132] = 
	{
		ID = 10132,
		MonsterID = 29,
		Name = "刑天·干",
		DescTitle = "混沌",
		DescText = "<Text_3_W>诞生于永恒之河的混沌中，与仇恨相约，</>",
		FileImg = "T_XT_01",
	},
	[10133] = 
	{
		ID = 10133,
		MonsterID = 29,
		Name = "刑天·干",
		DescTitle = "坚盾",
		DescText = "<Text_3_W>手执重盾，被愤恨所燃烧，</>",
		FileImg = "T_XT_01",
	},
	[10134] = 
	{
		ID = 10134,
		MonsterID = 29,
		Name = "刑天·干",
		DescTitle = "归途",
		DescText = "<Text_3_T>至暗之日，重归安宁。</>",
		FileImg = "T_XT_01",
	},
	[10135] = 
	{
		ID = 10135,
		MonsterID = 29,
		Name = "刑天·干",
		DescTitle = "前朝文档碎片1",
		DescText = "<Text_3_T>我们用盾牌捍卫皇室，我们用长枪刺穿敌人。</>\n<Text_3_T>我们的职责没有止息，我们的效忠死而后已。</>",
		FileImg = "T_XT_01",
	},
	[10136] = 
	{
		ID = 10136,
		MonsterID = 29,
		Name = "刑天·干",
		DescTitle = "善见未解之谜6",
		DescText = "<Text_3_W>目击报告：零类接触，在白噪中看到监兵形态机甲的案例。天人议会严词驳斥了这类传闻，坚称监兵机甲具备无与伦比的稳定性。流言则认为</><Text_3_T>存在被白噪影响乃至于控制的监兵机甲存在</><Text_3_W>，这将对各类赛博探险造成巨大威胁。</>",
		FileImg = "T_XT_01",
	},
	[10137] = 
	{
		ID = 10137,
		MonsterID = 29,
		Name = "刑天·干",
		DescTitle = "赛博作战手册23",
		DescText = "<Text_3_W>不要被它古旧甚至破损的外观所欺骗，这些机甲仍然保持着</><Text_3_T>十分强劲的出力</><Text_3_W>，其破坏力与监兵机甲不相上下。故而在应对策略上亦与突击监兵类似。</>",
		FileImg = "T_XT_01",
	},
	[10138] = 
	{
		ID = 10138,
		MonsterID = 30,
		Name = "刑天·戚",
		DescTitle = "归途",
		DescText = "<Text_3_W>降生于喧嚣之中，走向永恒宁静，</>",
		FileImg = "T_XT_02",
	},
	[10139] = 
	{
		ID = 10139,
		MonsterID = 30,
		Name = "刑天·戚",
		DescTitle = "安魂曲",
		DescText = "<Text_3_T>丧钟再度奏鸣，永无宁日，</>",
		FileImg = "T_XT_02",
	},
	[10140] = 
	{
		ID = 10140,
		MonsterID = 30,
		Name = "刑天·戚",
		DescTitle = "余音",
		DescText = "<Text_3_W>与暗夜之中，聆听诡境余音。</>",
		FileImg = "T_XT_02",
	},
	[10141] = 
	{
		ID = 10141,
		MonsterID = 30,
		Name = "刑天·戚",
		DescTitle = "前朝文档碎片2",
		DescText = "<Text_3_T>帝国的权威至高无上，帝国的律法公正无双。</>\n<Text_3_T>我们惶恐地接过帝胄的权柄，将它的荣宠与威仪四境传扬。</>",
		FileImg = "T_XT_02",
	},
	[10142] = 
	{
		ID = 10142,
		MonsterID = 30,
		Name = "刑天·戚",
		DescTitle = "善见未解之谜7",
		DescText = "<Text_3_W>目击报告：第二类接触，两个监兵形态机甲相互搏斗的目击报告。天人议会再次驳斥了相关传闻，原视频已被删除。针对奥秘科技的恩德系列机甲是否</><Text_3_T>另有源头</><Text_3_W>的讨论甚嚣尘上，对相关话题的赛博言论监管正在升级。</>",
		FileImg = "T_XT_02",
	},
	[10143] = 
	{
		ID = 10143,
		MonsterID = 30,
		Name = "刑天·戚",
		DescTitle = "赛博作战手册24",
		DescText = "<Text_3_W>有证据显示为机甲单位配备重型战斧的行为是从刑天开始，这也能解释为何它们的战斗技艺如此纯熟。不要掉以轻心，</><Text_3_T>旧帝国的处刑人不会给你第二次机会</><Text_3_W>。</>",
		FileImg = "T_XT_02",
	},
	[10144] = 
	{
		ID = 10144,
		MonsterID = 31,
		Name = "刑天·炮",
		DescTitle = "先行",
		DescText = "<Text_3_W>在战火和硝烟中，行走得比仇恨和战意更远，</>",
		FileImg = "T_XT_03",
	},
	[10145] = 
	{
		ID = 10145,
		MonsterID = 31,
		Name = "刑天·炮",
		DescTitle = "裁决者",
		DescText = "<Text_3_W>手中重武，即是对罪孽的裁决，</>",
		FileImg = "T_XT_03",
	},
	[10146] = 
	{
		ID = 10146,
		MonsterID = 31,
		Name = "刑天·炮",
		DescTitle = "永夜囚徒",
		DescText = "<Text_3_W>将一切罪孽与仇恨，囚禁于</><Text_3_T>永恒轮回的暗夜</><Text_3_W>之中。</>",
		FileImg = "T_XT_03",
	},
	[10147] = 
	{
		ID = 10147,
		MonsterID = 31,
		Name = "刑天·炮",
		DescTitle = "前朝文档碎片3",
		DescText = "<Text_3_T>我们大步向前行军，肩上钢枪寒光烁烁。</>\n<Text_3_T>行道树也屈身问候，因为我们一心为国。</>",
		FileImg = "T_XT_03",
	},
	[10148] = 
	{
		ID = 10148,
		MonsterID = 31,
		Name = "刑天·炮",
		DescTitle = "善见未解之谜8",
		DescText = "<Text_3_W>目击报告：第二类接触，监兵形态机甲射杀大群低级眷族的目击报告。天人议会声称这是枪炮监兵某日歼灭眷族的行动。目击者声称听到了</><Text_3_T>有节律的沉闷歌声</><Text_3_W>，语言并非现在常人所用。</>",
		FileImg = "T_XT_03",
	},
	[10149] = 
	{
		ID = 10149,
		MonsterID = 31,
		Name = "刑天·炮",
		DescTitle = "赛博作战手册25",
		DescText = "<Text_3_W>背后袭击虽然不雅但是十分有效，对付刑天这样庞大的机甲，</><Text_3_T>及时移动到其火力盲区后输出伤害</><Text_3_W>是合适的选择。</>",
		FileImg = "T_XT_03",
	},
	[10150] = 
	{
		ID = 10150,
		MonsterID = 32,
		Name = "暴走极光",
		DescTitle = "一心不乱",
		DescText = "<Text_3_W>极光都是很单纯的，都是为了</><Text_3_T>挣钱</><Text_3_W>而生的，</>\n<Text_3_W>不要憎恨她，要爱她，</>\n<Text_3_T>你与她也无差。</>",
		FileImg = "T_JG_02",
	},
	[10151] = 
	{
		ID = 10151,
		MonsterID = 32,
		Name = "暴走极光",
		DescTitle = "双面硬币",
		DescText = "<Text_3_W>金币叮咚一响，</><Text_3_T>机械通了人性</><Text_3_W>，</>\n<Text_3_W>金币叮咚一响，</><Text_3_T>人心化作铁石</><Text_3_W>，</>\n<Text_3_W>多神奇的金币。</>",
		FileImg = "T_JG_02",
	},
	[10152] = 
	{
		ID = 10152,
		MonsterID = 32,
		Name = "暴走极光",
		DescTitle = "三种欲望",
		DescText = "<Text_3_W>人有三种欲望，</><Text_3_T>金钱欲，金钱欲，金钱欲</><Text_3_W>，</>\n<Text_3_W>怎么都是金钱欲？你又没说是哪个人，</>\n<Text_3_W>反正我是。</>",
		FileImg = "T_JG_02",
	},
	[10153] = 
	{
		ID = 10153,
		MonsterID = 32,
		Name = "暴走极光",
		DescTitle = "机甲知识4",
		DescText = "<Text_3_W>极光全称「全环境自主决策性销售AI集成机器人系统」，由耶梦加得网络研发，意在在任何场合无死角提供购物服务。「极光造型可爱，内心同样如此，她被设计成</><Text_3_T>对人类没有任何恶意</><Text_3_W>，大家可以放心照顾她的生意。」——耶梦加得新闻官发布。</>",
		FileImg = "T_JG_02",
	},
	[10154] = 
	{
		ID = 10154,
		MonsterID = 32,
		Name = "暴走极光",
		DescTitle = "善见未解之谜9",
		DescText = "<Text_3_W>目击报告：第三类接触，赛博冒险者被发疯的极光殴打。耶梦加得已将相关讨论和网页全部删除。当事人表示自己向极光两次请求折扣，极光突然变成红色并开始用拳头殴打当事人。</><Text_3_T>很难想象温柔可人的极光会做此事</><Text_3_W>，坊间大多认为这是当事人暴力砍价未果后的碰瓷行为，而耶梦加得内部据信将之归咎于</><Text_3_T>某种古神病毒深度感染导致的人工智能失控</><Text_3_W>。</>",
		FileImg = "T_JG_02",
	},
	[10155] = 
	{
		ID = 10155,
		MonsterID = 32,
		Name = "暴走极光",
		DescTitle = "赛博作战手册26",
		DescText = "<Text_3_W>离吱吱作响的水壶远点，对暴走极光来说同理：</><Text_3_T>尽量让自己置身于极光拳头所及范围之外</><Text_3_W>，避免被极光的连续快拳打到。千万别因为她身材小而小看她，她可是经常无故殴打顾客的知名狠人。</>",
		FileImg = "T_JG_02",
	},
	[10156] = 
	{
		ID = 10156,
		MonsterID = 33,
		Name = "相思傀儡",
		DescTitle = "挂着",
		DescText = "<Text_3_W>所以再等等，</>\n<Text_3_W>不必慌张，</>\n<Text_3_W>对不起哦，这没用，</>\n<Text_3_T>能感受到我的爱吗？</>\n<Text_3_W>所以再等等。</>",
		FileImg = "T_XSKL_01",
	},
	[10157] = 
	{
		ID = 10157,
		MonsterID = 33,
		Name = "相思傀儡",
		DescTitle = "太久了",
		DescText = "<Text_3_W>红色的琴弦，</>\n<Text_3_W>猎物跑向猎人，</>\n<Text_3_W>带着天真的谎言诚实地等待，</>\n<Text_3_T>徒劳无功。</>",
		FileImg = "T_XSKL_01",
	},
	[10158] = 
	{
		ID = 10158,
		MonsterID = 33,
		Name = "相思傀儡",
		DescTitle = "权责一致",
		DescText = "<Text_3_W>春又来看红豆开，不见有情人去采，</>\n<Text_3_T>有情人不采，便采有情人。</>",
		FileImg = "T_XSKL_01",
	},
	[10159] = 
	{
		ID = 10159,
		MonsterID = 33,
		Name = "相思傀儡",
		DescTitle = "眷族观察手记2",
		DescText = "<Text_3_W>一只由红色光纤绑住身体部件而构成的、类似蜘蛛的机械生物，主体分为傀儡、主体两个结构：下半部傀儡结构是扭曲的机械人体，有大量红色的光线缠绕其腰部，少量红色光纤缠绕四肢关节；主体是蜘蛛的腹部，中央是一个缠绕满红色光纤的球状物，球状物的缝隙中，有个略微凸出的机械眼球。</>\n<Text_3_W>威胁等级：</><Text_3_T>极高</>",
		FileImg = "T_XSKL_01",
	},
	[10160] = 
	{
		ID = 10160,
		MonsterID = 33,
		Name = "相思傀儡",
		DescTitle = "善见未解之谜10",
		DescText = "<Text_3_W>目击报告：第二类接触，七个天选者部队在白噪中被蜘蛛丝样丝线捆绑悬空，场面极为诡异可怖。天人议会驳斥了相关传闻。</><Text_3_T>但随即有人目击大批天选者部队与监兵机甲进入白噪</><Text_3_W>，后续发展不明。</>",
		FileImg = "T_XSKL_01",
	},
	[10161] = 
	{
		ID = 10161,
		MonsterID = 33,
		Name = "相思傀儡",
		DescTitle = "赛博作战手册27",
		DescText = "<Text_3_W>相思傀儡是狡猾的对手，它最具威胁的时刻是脱离你的视线的时候——</><Text_3_T>注意头顶！</><Text_3_W>保持机动，躲避蛛丝和利爪，我们有机会打倒它。</>",
		FileImg = "T_XSKL_01",
	},
	[10162] = 
	{
		ID = 10162,
		MonsterID = 34,
		Name = "鸦天狗",
		DescTitle = "乌鸦还是狗",
		DescText = "<Text_3_W>「如果一只怪物有乌鸦的头，乌鸦的翅膀，乌鸦的脚，那它为什么不叫乌鸦，而要叫鸦天狗呢？」</>\n<Text_3_W>「朋友，这可能是因为你没有</><Text_3_T>掀开他们的面具</><Text_3_W>认真看一看。」</>\n<Text_3_W>「你亲眼见过吗？」</>\n<Text_3_W>「当然……嗯，当然是见过电子版的。」</>",
		FileImg = "T_YTG_01",
	},
	[10163] = 
	{
		ID = 10163,
		MonsterID = 34,
		Name = "鸦天狗",
		DescTitle = "支线任务",
		DescText = "<Text_3_W>鸦天狗通常用尖利的脚爪吸引人类的注意力，让对方下意识地躲避他们的袭击，随后他们再用锋利的羽翼从侧面攻击，因此资深的深潜爱好者通常会</><Text_3_T>避免与他们产生冲突</><Text_3_W>。</>",
		FileImg = "T_YTG_01",
	},
	[10164] = 
	{
		ID = 10164,
		MonsterID = 34,
		Name = "鸦天狗",
		DescTitle = "高级物理",
		DescText = "<Text_3_W>鸦天狗并不依靠视觉感知猎物，他们的羽翼能够感受</><Text_3_T>极为微弱的气流震动</><Text_3_W>，从而迅速定位猎物的体积和方位，并发起快速攻击。</>",
		FileImg = "T_YTG_01",
	},
	[10165] = 
	{
		ID = 10165,
		MonsterID = 34,
		Name = "鸦天狗",
		DescTitle = "眷族观察手记3",
		DescText = "<Text_3_W>形态接近翼龙，腹部有类似巨型藤壶的机械眼球，飞翔时会周期性坠落，爆裂产生粘液和伤害（极度危险！）。颈部细长，头部较大，喙长且宽。头部的前半段形似机械面具，侧面接近后脑处有明显的接缝结构。双手较长，手腕和腋下间有薄而锋利的翅，翅的结构近似分瓣、长而硬的羽翅。</>\n<Text_3_W>威胁等级：</><Text_3_T>极高</>",
		FileImg = "T_YTG_01",
	},
	[10166] = 
	{
		ID = 10166,
		MonsterID = 34,
		Name = "鸦天狗",
		DescTitle = "善见未解之谜11",
		DescText = "<Text_3_W>目击报告：第一类接触，白噪中出现不明飞行物。天人议会正在核查相关事实，</><Text_3_T>据信正在推进防空型机甲的招标工作</><Text_3_W>。</>",
		FileImg = "T_YTG_01",
	},
	[10167] = 
	{
		ID = 10167,
		MonsterID = 34,
		Name = "鸦天狗",
		DescTitle = "赛博作战手册28",
		DescText = "<Text_3_W>由于对空武器的缺乏，想要攻击高飞在天的鸦天狗几乎不可能，好在它们为了攻击你还是会</><Text_3_T>降落</><Text_3_W>。在躲开它们的第一波攻击后对发起迅捷的攻击，我们就能把这些骄傲的飞行员掀翻在地。</>",
		FileImg = "T_YTG_01",
	},
	[10168] = 
	{
		ID = 10168,
		MonsterID = 35,
		Name = "怒之般若",
		DescTitle = "较低攻击性",
		DescText = "<Text_3_W>在白噪中遭遇这种怪物通常不会让人感到恐惧，他们</><Text_3_T>攻击人类的欲望较低</><Text_3_W>，只要不主动与它们发生冲突通常都能平安脱身。</>",
		FileImg = "T_TKMJ_01",
	},
	[10169] = 
	{
		ID = 10169,
		MonsterID = 35,
		Name = "怒之般若",
		DescTitle = "多种假说",
		DescText = "<Text_3_W>般若奇特的断角形态有诸多假说，有学者提出这是他们在族群内部冲突过程中造成的损伤，也有人认为这是他们对于能量使用的一种特殊形式，将有限的能量利用在</><Text_3_T>自身功能的维稳</><Text_3_W>上，而不是用于攻击部位的构造。</>",
		FileImg = "T_TKMJ_01",
	},
	[10170] = 
	{
		ID = 10170,
		MonsterID = 35,
		Name = "怒之般若",
		DescTitle = "赛博手办",
		DescText = "<Text_3_W>一些品位怪异的深潜爱好者，用3D打印技术将般若的造型制作成各种手办，并表示这能</><Text_3_T>「庇护他们在深潜中免受理智伤害」</><Text_3_W>。这一小众爱好并未广泛流传，而他们的这一说法更是无法得到证实。</>",
		FileImg = "T_TKMJ_01",
	},
	[10171] = 
	{
		ID = 10171,
		MonsterID = 35,
		Name = "怒之般若",
		DescTitle = "眷族观察手记4",
		DescText = "<Text_3_W>鬼面具形式的低级眷族，似乎不具备智能，通过向前冲撞制造伤害。似乎在某些龙形眷族身上看到过类似结构。往往与面灵气一同出现，或许存在隶属关系。</>\n<Text_3_W>威胁等级：</><Text_3_T>低</>",
		FileImg = "T_TKMJ_01",
	},
	[10172] = 
	{
		ID = 10172,
		MonsterID = 35,
		Name = "怒之般若",
		DescTitle = "善见未解之谜12",
		DescText = "<Text_3_W>目击报告：第一类接触，数个般若在白噪中组成环形转圈。天人议会发出公告，不鼓励无关人等为探索这种无关紧要的事冒险进入白噪，违者罚款。</>",
		FileImg = "T_TKMJ_01",
	},
	[10173] = 
	{
		ID = 10173,
		MonsterID = 35,
		Name = "怒之般若",
		DescTitle = "赛博作战手册29",
		DescText = "<Text_3_W>打败你的不是般若，是面对般若时的</><Text_3_T>松懈</><Text_3_W>。拿出对付其他大型单位时的警惕，不要轻视它发起的每一次撞击，及时躲避，消灭它是水到渠成之事。</>",
		FileImg = "T_TKMJ_01",
	},
	[10174] = 
	{
		ID = 10174,
		MonsterID = 36,
		Name = "怨之般若",
		DescTitle = "学术讨论",
		DescText = "<Text_3_W>当学者们首次在白噪中观测到这种奇特的机械生物后，便引发了持久的关于</><Text_3_T>「它们究竟是寄生生物还是共生生物」</><Text_3_W>的讨论。</>",
		FileImg = "T_BR_01",
	},
	[10175] = 
	{
		ID = 10175,
		MonsterID = 36,
		Name = "怨之般若",
		DescTitle = "自我迭代",
		DescText = "<Text_3_W>主流的观点通常认为原本初级的般若均为单独行动，但在漫长的演化过程中，渐渐形成了这种奇特的</><Text_3_T>联合共生</><Text_3_W>的关系。</>",
		FileImg = "T_BR_01",
	},
	[10176] = 
	{
		ID = 10176,
		MonsterID = 36,
		Name = "怨之般若",
		DescTitle = "组合优化",
		DescText = "<Text_3_W>根据学者们的实验表明：如果人为切断三个般若个体之间的线缆连接，他们在一定时间内依旧会</><Text_3_T>自动聚集</><Text_3_W>起来，重新变回一个聚合的整体。</>",
		FileImg = "T_BR_01",
	},
	[10177] = 
	{
		ID = 10177,
		MonsterID = 36,
		Name = "怨之般若",
		DescTitle = "急需联调",
		DescText = "<Text_3_W>深潜探索者经常会观测到聚合形态的般若会进入短暂的行动暂停状态，让他们有机会可以脱离对方的攻击，这可能是呈组合形态的般若的</><Text_3_T>神经同步率尚未完全完善</><Text_3_W>的原因。</>",
		FileImg = "T_BR_01",
	},
	[10178] = 
	{
		ID = 10178,
		MonsterID = 36,
		Name = "怨之般若",
		DescTitle = "泡泡枪",
		DescText = "<Text_3_W>般若奇特的攻击方式会给人留下深刻印象：从面具中快速发射出多枚</><Text_3_T>气泡状</><Text_3_W>的武器，这通常会让不熟悉他们的深潜探索者降低戒备，误以为这些气泡没有伤害性。</>",
		FileImg = "T_BR_01",
	},
	[10179] = 
	{
		ID = 10179,
		MonsterID = 36,
		Name = "怨之般若",
		DescTitle = "强迫症",
		DescText = "<Text_3_W>般若的组合形态通常由</><Text_3_T>红、绿、白</><Text_3_W>三种般若个体组合共生，这可能是因为这些个体具有更好的同步联调率。但有一些先锋艺术家始终对于这种生物的存在耿耿于怀：「它们为什么不是三原色组合在一起！」</>",
		FileImg = "T_BR_01",
	},
	[10180] = 
	{
		ID = 10180,
		MonsterID = 38,
		Name = "贪之般若",
		DescTitle = "稀缺掉率",
		DescText = "<Text_3_W>贪之般若似乎是全类型般若中最为罕见的一种，通体</><Text_3_T>金色</><Text_3_W>的光泽给人留下非常深的印象。</>",
		FileImg = "T_BR_02",
	},
	[10181] = 
	{
		ID = 10181,
		MonsterID = 38,
		Name = "贪之般若",
		DescTitle = "信息共享",
		DescText = "<Text_3_W>一般认为三个般若高频率地共享探测到的周围环境的线索，以此迅速定位，并灵活地调节自身的行动路线和</><Text_3_T>躲避追猎者</><Text_3_W>的策略。</>",
		FileImg = "T_BR_02",
	},
	[10182] = 
	{
		ID = 10182,
		MonsterID = 38,
		Name = "贪之般若",
		DescTitle = "趋之若鹜",
		DescText = "<Text_3_W>深潜探险者通常非常渴望能够在赛博空间里遇到它们，根据他们的传言：这种怪物通常携带了大量</><Text_3_T>罕见代码和数据</><Text_3_W>，能够在黑市交易出不错的价格。</>",
		FileImg = "T_BR_02",
	},
	[10183] = 
	{
		ID = 10183,
		MonsterID = 38,
		Name = "贪之般若",
		DescTitle = "眷族观察手记5",
		DescText = "<Text_3_W>外形同为般若面具，但是装饰以金色，似乎没有任何武装配备。在赛博空间中似乎占据清理者的生态位，因此包含大量</><Text_3_T>高价值数据</><Text_3_W>。</>\n<Text_3_W>威胁等级：</><Text_3_T>极低。</>",
		FileImg = "T_BR_02",
	},
	[10184] = 
	{
		ID = 10184,
		MonsterID = 38,
		Name = "贪之般若",
		DescTitle = "善见未解之谜14",
		DescText = "<Text_3_W>目击报告：第三类接触，数个赛博探险者将般若当球踢。天人议会谴责这种不尊重其他生物的行为，要求限制赛博探险者</><Text_3_T>肆意前往赛博空间狩猎贪之般若</><Text_3_W>的状况。</>",
		FileImg = "T_BR_02",
	},
	[10185] = 
	{
		ID = 10185,
		MonsterID = 38,
		Name = "贪之般若",
		DescTitle = "赛博作战手册31",
		DescText = "<Text_3_W>你怎么会被这玩意击晕的？被金光晃到眼睛了吗？</>",
		FileImg = "T_BR_02",
	},
	[10186] = 
	{
		ID = 10186,
		MonsterID = 39,
		Name = "面灵气之苏生",
		DescTitle = "低功耗",
		DescText = "<Text_3_W>这种怪物在白噪中的出现令人不安，他们的面具彼此分散，移动时</><Text_3_T>不会发出丝毫声音</><Text_3_W>。</>",
		FileImg = "T_MLQ_01",
	},
	[10187] = 
	{
		ID = 10187,
		MonsterID = 39,
		Name = "面灵气之苏生",
		DescTitle = "排列组合",
		DescText = "<Text_3_W>研究者们很难解释在面灵气的同一个生物体上，同时具有线缆链接和类似</><Text_3_T>磁悬浮链接</><Text_3_W>的不同形式。</>",
		FileImg = "T_MLQ_01",
	},
	[10188] = 
	{
		ID = 10188,
		MonsterID = 39,
		Name = "面灵气之苏生",
		DescTitle = "群体智能",
		DescText = "<Text_3_W>面灵气的移动路径通常由体型最大的面具驱动，似乎具有一定的</><Text_3_T>群体智能性</><Text_3_W>。</>",
		FileImg = "T_MLQ_01",
	},
	[10189] = 
	{
		ID = 10189,
		MonsterID = 39,
		Name = "面灵气之苏生",
		DescTitle = "眷族观察手记6",
		DescText = "<Text_3_W>由多个机械面具构成的生命体，类似不规则的葡萄串，有导管连接各个面具，在漂浮在空中时有类似呼吸的收缩——舒展动作。自身没有攻击力，会从虚空之中召唤怒之般若，应当谨慎对待。</>\n<Text_3_W>威胁等级：</><Text_3_T>中</>",
		FileImg = "T_MLQ_01",
	},
	[10190] = 
	{
		ID = 10190,
		MonsterID = 39,
		Name = "面灵气之苏生",
		DescTitle = "善见未解之谜15",
		DescText = "<Text_3_W>目击报告：第一类接触，接市民报案前来清理般若的天选组成员发现般若数量是报案者所说的三倍且仍在不断增加，天选组成员选择直接撤退，此事成为笑谈。</>",
		FileImg = "T_MLQ_01",
	},
	[10191] = 
	{
		ID = 10191,
		MonsterID = 39,
		Name = "面灵气之苏生",
		DescTitle = "赛博作战手册32",
		DescText = "<Text_3_W>你怎么会被这玩意击晕的？看见般若下蛋吓到了吗？</>",
		FileImg = "T_MLQ_01",
	},
	[10192] = 
	{
		ID = 10192,
		MonsterID = 40,
		Name = "面灵气之加护",
		DescTitle = "红色恶兆",
		DescText = "<Text_3_W>红色的面灵气出现通常预示着可能会出现</><Text_3_T>更高烈度的白噪</><Text_3_W>。</>",
		FileImg = "T_MLQ_02",
	},
	[10193] = 
	{
		ID = 10193,
		MonsterID = 40,
		Name = "面灵气之加护",
		DescTitle = "急速出击",
		DescText = "<Text_3_W>相比普通形态的面灵气，红色的面灵气</><Text_3_T>移动速度更快、灵敏性更高</><Text_3_W>，处理起来也更麻烦。</>",
		FileImg = "T_MLQ_02",
	},
	[10194] = 
	{
		ID = 10194,
		MonsterID = 40,
		Name = "面灵气之加护",
		DescTitle = "记忆混乱",
		DescText = "<Text_3_W>根据大数据显示，红色面灵气的出现概率约为15.7%，但很多白噪中的求助通讯的描述通常是「我在雾中见到了</><Text_3_T>一堆红色的面具</><Text_3_W>」，这可能是红色的面灵气在白噪中可辨识度更高的原因，因此给目击者留下了更为深刻的印象。</>",
		FileImg = "T_MLQ_02",
	},
	[10195] = 
	{
		ID = 10195,
		MonsterID = 40,
		Name = "面灵气之加护",
		DescTitle = "眷族观察手记6",
		DescText = "<Text_3_W>由多个机械面具构成的生命体，类似不规则的葡萄串，有导管连接各个面具，在漂浮在空中时有类似呼吸的收缩——舒展动作。自身没有攻击力，会为其他个体施加数据护盾，应当谨慎对待。</>\n<Text_3_W>威胁等级：</><Text_3_T>低</>",
		FileImg = "T_MLQ_02",
	},
	[10196] = 
	{
		ID = 10196,
		MonsterID = 40,
		Name = "面灵气之加护",
		DescTitle = "善见未解之谜15",
		DescText = "<Text_3_W>目击报告：第三类接触，一名白刀队员攻击一只怒之般若，但每次击破数据护盾时都会被后面的面灵气重新布置护盾，陷入死循环中。该视频流传甚远，往往被当做嘲笑白刀队缺乏智慧的佐证。</>",
		FileImg = "T_MLQ_02",
	},
	[10197] = 
	{
		ID = 10197,
		MonsterID = 40,
		Name = "面灵气之加护",
		DescTitle = "赛博作战手册32",
		DescText = "<Text_3_W>你怎么会被这玩意击晕的？看见般若套盾吓到了吗？</>",
		FileImg = "T_MLQ_02",
	},
	[10198] = 
	{
		ID = 10198,
		MonsterID = 41,
		Name = "京观",
		DescTitle = "好大的脸",
		DescText = "<Text_3_W>很难分辨京观的正面和背面，因为它们通常由</><Text_3_T>大量的脸部形态的面具</><Text_3_W>堆叠组成，没有明显的方向性。</>",
		FileImg = "T_JG_03",
	},
	[10199] = 
	{
		ID = 10199,
		MonsterID = 41,
		Name = "京观",
		DescTitle = "复眼定位法",
		DescText = "<Text_3_W>京观的每一部分面具上都有</><Text_3_T>独立的眼睛</><Text_3_W>，这有助于他们更好地定位方向和位置。</>",
		FileImg = "T_JG_03",
	},
	[10200] = 
	{
		ID = 10200,
		MonsterID = 41,
		Name = "京观",
		DescTitle = "红色噩梦",
		DescText = "<Text_3_W>在白噪中遭遇京观的人类通常会陷入歇斯底里的状态，并宣称自己「在雾中看到了很多</><Text_3_T>发着红光、漂浮的眼睛</><Text_3_W>」。</>",
		FileImg = "T_JG_03",
	},
	[10201] = 
	{
		ID = 10201,
		MonsterID = 41,
		Name = "京观",
		DescTitle = "眷族观察手记7",
		DescText = "<Text_3_W>由多个机械面具构成的巨大悬浮球体，包含7个较大的面具和多个小型面具，表面凹凸犹如肿瘤，十分可怖。通过散开面具布置出一片环形区域，发射激光对区域内个体造成伤害。</>\n<Text_3_W>威胁等级：</><Text_3_T>高</>",
		FileImg = "T_JG_03",
	},
	[10202] = 
	{
		ID = 10202,
		MonsterID = 41,
		Name = "京观",
		DescTitle = "善见未解之谜16",
		DescText = "<Text_3_W>目击报告：第三类接触，数个来自白刀队员的报告，他们在面对某种眷族时对象突然消失，随即分裂成数个小的面具将白刀队员包围并发射激光，造成数人重伤。天人议会表彰了这些队员付出的牺牲，并以之为案例警告市民</><Text_3_T>不要贸然进入白噪</><Text_3_W>。</>",
		FileImg = "T_JG_03",
	},
	[10203] = 
	{
		ID = 10203,
		MonsterID = 41,
		Name = "京观",
		DescTitle = "赛博作战手册33",
		DescText = "<Text_3_W>不要因为京观突然消失而掉以轻心，这是它们</><Text_3_T>布置阵型攻击你的前奏</><Text_3_W>，随时保持移动，直到京观再次现身。</>",
		FileImg = "T_JG_03",
	},
	[10204] = 
	{
		ID = 10204,
		MonsterID = 43,
		Name = "饕餮",
		DescTitle = "简单高效",
		DescText = "<Text_3_W>螺钉、机械、齿轮，组合起来可以成为驱动系统，当然也可以成为一只名为饕餮的怪物。</>",
		FileImg = "T_TT_01",
	},
	[10205] = 
	{
		ID = 10205,
		MonsterID = 43,
		Name = "饕餮",
		DescTitle = "白噪凶险",
		DescText = "<Text_3_W>根据有限的观测数据显示：饕餮喜爱在白噪中出没，</><Text_3_T>出没频率与白噪烈度成显著正相关</><Text_3_W>。</>",
		FileImg = "T_TT_01",
	},
	[10206] = 
	{
		ID = 10206,
		MonsterID = 43,
		Name = "饕餮",
		DescTitle = "饕餮之口",
		DescText = "<Text_3_W>饕餮喜爱捕食更为小型的眷族，有时甚至会伤害比自己体型小的同类，</><Text_3_T>但没有数据证明他们对有机生命体表现出兴趣</><Text_3_W>。</>",
		FileImg = "T_TT_01",
	},
	[10207] = 
	{
		ID = 10207,
		MonsterID = 43,
		Name = "饕餮",
		DescTitle = "眷族观察手记7",
		DescText = "<Text_3_W>类似巨大鬣狗的机械生物，体型远远超过现存最大的犬科动物。拥有强壮的脖颈和巨大的、延伸到脖子的嘴，里面藏满机械牙齿。嘴内有激光发射器，可以释放可观的能量攻击。以上种种结合起来，令身形矫健的它拥有巨大的杀伤力。</>\n<Text_3_W>威胁等级：</><Text_3_T>极高</>",
		FileImg = "T_TT_01",
	},
	[10208] = 
	{
		ID = 10208,
		MonsterID = 43,
		Name = "饕餮",
		DescTitle = "善见未解之谜16",
		DescText = "<Text_3_W>目击报告：第三类接触，一支天选组部队在白噪内被歼灭，回收的记录仪显示有且仅有一只饕餮参与战斗。天人议会</><Text_3_T>已将事发地点封锁为禁区</><Text_3_W>。</>",
		FileImg = "T_TT_01",
	},
	[10209] = 
	{
		ID = 10209,
		MonsterID = 43,
		Name = "饕餮",
		DescTitle = "赛博作战手册33",
		DescText = "<Text_3_W>面对这一等级的威胁，最好的选择是拔腿就跑。如果一定要战斗的话，注意它挥舞利爪与使用激光炮的节奏，在其攻击的空窗期内发起攻击。</><Text_3_T>绝对不要因贪图制造更多伤害而忽视躲避接下来的攻击</><Text_3_W>，饕餮不会给你这样的机会！</>",
		FileImg = "T_TT_01",
	},
	[10210] = 
	{
		ID = 10210,
		MonsterID = 45,
		Name = "意外惊喜",
		DescTitle = "普罗软件杂志1",
		DescText = "<Text_3_W>以最佳密度布置在你的赛博宝藏附近，每一颗都与数据世界浑然一体，秘密武器「赛博爆破」更给不速之客意外惊喜呀！</>",
		FileImg = "T_YWJX",
	},
	[10211] = 
	{
		ID = 10211,
		MonsterID = 46,
		Name = "不要抬头",
		DescTitle = "普罗软件杂志2",
		DescText = "<Text_3_W>你看，多么蓝的天啊，一直往前走，不要抬头，你就会和赛博空间「融为一体」......中啦！</>",
		FileImg = "T_BYTT",
	},
	[10212] = 
	{
		ID = 10212,
		MonsterID = 47,
		Name = "热锅英雄",
		DescTitle = "普罗软件杂志3",
		DescText = "<Text_3_W>*不速之客正尝试在高温区域游泳，不要学他*</>",
		FileImg = "T_RGYX",
	},
	[10213] = 
	{
		ID = 10213,
		MonsterID = 48,
		Name = "电光信仰",
		DescTitle = "普罗软件杂志4",
		DescText = "<Text_3_W>地面上闪烁的电光，是我们不灭的信仰！释放吧！为了保护您的隐私数据安全！</>",
		FileImg = "T_YWJX",
	},
	[10214] = 
	{
		ID = 10214,
		MonsterID = 50,
		Name = "红红火火",
		DescTitle = "普罗软件杂志5",
		DescText = "<Text_3_W>燃起来了！燃起来了！哈哈哈，闯入者，现在你感觉如何？用最喜庆的方式保护你的数据安全！</>",
		FileImg = "T_HHHH",
	},
	[10215] = 
	{
		ID = 10215,
		MonsterID = 52,
		Name = "光凌大阵",
		DescTitle = "普罗软件杂志6",
		DescText = "<Text_3_W>把你童年最喜欢的RTS游戏搬到赛博空间中，像保护你的基地一样保护隐私数据吧！告诉那些数据小偷1+1真的大于2！</>",
		FileImg = "T_GLDZ",
	},
	[10216] = 
	{
		ID = 10216,
		MonsterID = 23,
		Name = "彼岸无常",
		DescTitle = "花开花落",
		DescText = "<Text_3_W>传闻彼岸花开一千年，落一千年。</>\n<Text_3_W>但这朵鲜红的机械彼岸花，永远不会凋谢。</>",
		FileImg = "T_BAWC",
	},
	[10217] = 
	{
		ID = 10217,
		MonsterID = 23,
		Name = "彼岸无常",
		DescTitle = "等价交换",
		DescText = "<Text_3_W>过去的回忆不会随着时光消散，我已经将你的记忆都留存在了彼岸花里。</>\n<Text_3_W>想要唤醒你过去的回忆吗？那么，就用你的生命来和我交换。</>",
		FileImg = "T_BAWC",
	},
	[10218] = 
	{
		ID = 10218,
		MonsterID = 23,
		Name = "彼岸无常",
		DescTitle = "引路人",
		DescText = "<Text_3_W>迷失在白噪里的旅人，跟随我前往彼岸的另一端。</>\n<Text_3_W>那里没有痛苦，没有迷惘。</>\n<Text_3_W>只需要你将自己的一切奉献给祂们。</>",
		FileImg = "T_BAWC",
	},
	[10219] = 
	{
		ID = 10219,
		MonsterID = 23,
		Name = "彼岸无常",
		DescTitle = "执念",
		DescText = "<Text_3_W>又为什么要执着于做一个人类呢？肉身苦弱，无法永恒。</>\n<Text_3_W>在弥漫白噪的彼岸，有着大片的机械彼岸花，还有你想要寻找的答案。</>",
		FileImg = "T_BAWC",
	},
	[10220] = 
	{
		ID = 10220,
		MonsterID = 23,
		Name = "彼岸无常",
		DescTitle = "缄默",
		DescText = "<Text_3_W>不需要说出你的答案，祂们已经了解了你的一切。</>",
		FileImg = "T_BAWC",
	},
	[10221] = 
	{
		ID = 10221,
		MonsterID = 23,
		Name = "彼岸无常",
		DescTitle = "化身为花",
		DescText = "<Text_3_W>你的生命，你的过去，你的一切，我都收下了。</>\n<Text_3_W>它们会在这片彼岸花里，得到永恒。</>",
		FileImg = "T_BAWC",
	},
	[10222] = 
	{
		ID = 10222,
		MonsterID = 44,
		Name = "附骨众",
		DescTitle = "利刃",
		DescText = "<Text_3_W>在敌人察觉之前，他们的双刀就已经封住了对方的咽喉。</>",
		FileImg = "T_FGZ",
	},
	[10223] = 
	{
		ID = 10223,
		MonsterID = 44,
		Name = "附骨众",
		DescTitle = "锁定",
		DescText = "<Text_3_W>他们不需要用视力锁定白噪中的敌人，极其敏锐的听觉就能让它们在雾中掌控一切。</>",
		FileImg = "T_FGZ",
	},
	[10224] = 
	{
		ID = 10224,
		MonsterID = 44,
		Name = "附骨众",
		DescTitle = "雾中人",
		DescText = "<Text_3_W>如果在白噪中迷失方向，又听到一种怪异而尖锐的声音时，不要犹豫，赶紧避险。</>\n<Text_3_W>那是他们尖利的刀刃刮擦在地面上的声音……</>",
		FileImg = "T_FGZ",
	},
	[10225] = 
	{
		ID = 10225,
		MonsterID = 44,
		Name = "附骨众",
		DescTitle = "前行",
		DescText = "<Text_3_W>头所在的方向，并不一定是前进的方向。</>\n<Text_3_W>因为他们的头已经在背后扭曲成一个古怪的角度。</>",
		FileImg = "T_FGZ",
	},
	[10226] = 
	{
		ID = 10226,
		MonsterID = 44,
		Name = "附骨众",
		DescTitle = "噩梦",
		DescText = "<Text_3_W>众多尖利的牙齿让他们的外貌极为古怪，曾在白噪目睹过他们的探险者都会陷入长久的噩梦中。</>",
		FileImg = "T_FGZ",
	},
	[10227] = 
	{
		ID = 10227,
		MonsterID = 44,
		Name = "附骨众",
		DescTitle = "一刀两断",
		DescText = "<Text_3_W>如果被众多附骨众所包围，那你的愿望最好是……希望他们给你来个痛快的。</>",
		FileImg = "T_FGZ",
	},
	[10228] = 
	{
		ID = 10228,
		MonsterID = 53,
		Name = "飞鱼",
		DescTitle = "超光速",
		DescText = "<Text_3_W>快速，还是快速，人类难以在白噪中看清飞鱼的体态。</>\n<Text_3_W>因为它们的速度实在是过于惊人。</>",
		FileImg = "T_FY",
	},
	[10229] = 
	{
		ID = 10229,
		MonsterID = 53,
		Name = "飞鱼",
		DescTitle = "秩序感",
		DescText = "<Text_3_W>有白噪探险者描述过自己的离奇经历：曾经目睹过大量飞鱼列队前进，如同人类的军队一般。</>\n<Text_3_W>通常领队的飞鱼体型更大，造型更浮夸，这似乎也与人类社会的习俗很类似。</>",
		FileImg = "T_FY",
	},
	[10230] = 
	{
		ID = 10230,
		MonsterID = 53,
		Name = "飞鱼",
		DescTitle = "拟态",
		DescText = "<Text_3_W>有人认为飞鱼的袭击方式很像蝎子，它们用尾部辅助攻击，极大增加自身战力。</>",
		FileImg = "T_FY",
	},
	[10231] = 
	{
		ID = 10231,
		MonsterID = 53,
		Name = "飞鱼",
		DescTitle = "隐身",
		DescText = "<Text_3_W>飞鱼在战斗过程中，经常以出其不意的方式跳跃起来，并瞬间消失在白噪中，伺机偷袭。这一举止非常容易迷惑敌人，让它们在接下来的袭击中占据上风。</>",
		FileImg = "T_FY",
	},
	[10232] = 
	{
		ID = 10232,
		MonsterID = 53,
		Name = "飞鱼",
		DescTitle = "液压驱动",
		DescText = "<Text_3_W>飞鱼的尾部具有极强的力量，甚至可以一击让一个成年人短暂失去意识，有科学家推测它们在进化过程中，尾部具备了独特的液压加强动力系统。</>",
		FileImg = "T_FY",
	},
	[10233] = 
	{
		ID = 10233,
		MonsterID = 53,
		Name = "飞鱼",
		DescTitle = "赶紧跑路",
		DescText = "<Text_3_W>如果当你目睹了三条以上的飞鱼时，你此时最有效的应对方式就是——快跑！不要回头！</>",
		FileImg = "T_FY",
	},
	[10234] = 
	{
		ID = 10234,
		MonsterID = 54,
		Name = "雷电修士",
		DescTitle = "天雷",
		DescText = "<Text_3_W>引动天雷，惩戒罪恶。</>",
		FileImg = "T_JYR",
	},
	[10235] = 
	{
		ID = 10235,
		MonsterID = 54,
		Name = "雷电修士",
		DescTitle = "故我",
		DescText = "<Text_3_W>静修本心，无我无界。</>",
		FileImg = "T_JYR",
	},
	[10236] = 
	{
		ID = 10236,
		MonsterID = 54,
		Name = "雷电修士",
		DescTitle = "断绝",
		DescText = "<Text_3_W>前尘无路，前缘已绝。</>",
		FileImg = "T_JYR",
	},
	[10237] = 
	{
		ID = 10237,
		MonsterID = 54,
		Name = "雷电修士",
		DescTitle = "隐世",
		DescText = "<Text_3_W>隐于白噪，静待神谕。</>",
		FileImg = "T_JYR",
	},
	[10238] = 
	{
		ID = 10238,
		MonsterID = 54,
		Name = "雷电修士",
		DescTitle = "聆听",
		DescText = "<Text_3_W>神明之召，自雾中起。</>",
		FileImg = "T_JYR",
	},
	[10239] = 
	{
		ID = 10239,
		MonsterID = 54,
		Name = "雷电修士",
		DescTitle = "戴罪之身",
		DescText = "<Text_3_W>戴罪之人，不得解脱。</>",
		FileImg = "T_JYR",
	},
}
'''

json_output = convert_to_json(data)

with open('Resources/MonsterInfoData.json', 'w', encoding='utf-8') as f:
    f.write(json_output)