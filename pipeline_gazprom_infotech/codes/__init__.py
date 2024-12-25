"""Infotech official dictionaries."""
from .pigtype import PigType
from .passtype import PassType
from .tube import Tube
from .company import Company
from .kbd import MethodsKBD
from .feature import Feature


NAME = {

  # PigType
  PigType.MFL: "Дефектоскоп магнитный продольного намагничивания",
  PigType.TFI: "Дефектоскоп магнитный поперечного намагничивания",
  PigType.CALIPER_MECH: "Рычажный (профилемер)",
  PigType.NAVIGATE: "Поршень навигационно-топографический",
  PigType.ULTRASONIC: "Ультразвуковой дефектоскоп",
  PigType.CALIPER_MAGN: "Магнитный профилемер",
  PigType.EMAP: "Дефектоскоп электромагнитный акустический",
  PigType.COMBO: "Комбинированный дефектоскоп",
  PigType.CLEANER: "Очистной скребок",
  PigType.CALIPER_TOOL: "Поршень-шаблон",

  # PassType
  PassType.COMPLEX: "Комплексное внутритрубное обследование",
  PassType.COMPLEX_SKS: "Комплексное внутритрубное обследование + СКС",
  PassType.COMPLEX_NAV: "Комплексное внутритрубное обследование+навигация",
  PassType.NAVIGATE: "Навигационно-профильное обследование",
  PassType.CALIPER: "Профильное обследование",
  PassType.TFI: "Стресc-коррозионное обследование",
  PassType.ULTRASONIC: "Ультразвуковое обследование (УЗК)",
  PassType.EXPERIMENTAL: "Экспериментальное обследование",
  PassType.EMAP: "ЭМАП-обследование",

  # Tube
  Tube.BEZSHOV: "Бесшовная",
  Tube.DVUSHOV: "Двухшовная",
  Tube.UNKNOWN: "Неопределенная секция",
  Tube.ODNOSHOV: "Одношовная",
  Tube.SPIRAL: "Спиралешовная",
  Tube.DIRECT: "Прямошовная",
  Tube.VALVE: "Кран-секция",
  Tube.BRANCH: "Тройник-секция",
  Tube.SEGMENT: "Сегментная вставка",
  Tube.CURVE0: "Отвод холодного гнутья бесшовный",
  Tube.CURVE1: "Отвод холодного гнутья одношовный",
  Tube.CURVE2: "Отвод холодного гнутья двухшовный",

  # Company
  Company.BSPC: "BSPC B.V",
  Company.AVTOGAZ: "Автогаз, ОАО",
  Company.AEROCOSM: "Аэрокосмический мониторинг и технологии, ЗАО",
  Company.BKH: "Бейкер Хьюз Технологии и трубопроводный сервис, АО",
  Company.GPAS: "Газприборавтоматикасервис, ЗАО",
  Company.DIASCAN: "ЦТД Диаскан, ОАО",
  Company.DIAPROM: "НТЦ Диапром, ООО",
  Company.OEG: "Оргэнергогаз, ОАО",
  Company.PODVGAZENERGO: "Подводгазэнергосервис, ООО",
  Company.PODVODDIAG: "Подводдиагностика, ООО",
  Company.PODVODSERV: "Подводсервис, ООО",
  Company.ROZEN: "Розен",
  Company.SNG: "НПО Спецнефтегаз, ЗАО",
  Company.TUBOSCAN: "Тьюбоскан, ООО",
  Company.VNUTRITRUBDIAG: "НПЦ Внутритрубная диагностика, ООО",

  Company.PIPETRONIX: "PII Пайптроникс",
  Company.VEZERFORD: "Везерфорд трубопроводный сервис, ЗАО",
  Company.GKSOOO: "Газкомплектсервис, ООО",
  Company.GAZPROEKT: "Газпроект-ДКР, ООО (г.Санкт-Петербург)",
  Company.GDIAG: "ИТЦ Саратов Газпром диагностика, АО",
  Company.IFDM: "ИФДМ, ООО",
  Company.INTERGAZ: "Интергаз Центральная Азия, ЗАО",
  Company.NGPERSP: "НефтеГазПерспектива, ООО",
  Company.NGKOMPLSERV: "Нефтегазкомплектсервис, ЗАО",
  Company.PROMTEH: "ОсОО «ПромТех-Эксперт»",
  Company.SELFMADE: "Собственными силами",
  Company.ENTE: "ЭНТЭ, ООО",
  Company.YOULTA: "Юлта, ООО",

  # MethodsKBD
  MethodsKBD.API579: "API 579 Трещины, Уровень 2",
  MethodsKBD.ASME: "ASME B31G-1991",
  MethodsKBD.BS7910: "BS 7910:2005",
  MethodsKBD.DNV: "DNV-RP-F101-2004",
  MethodsKBD.NGKS: "Методика определения опасности повреждений стенки трубопроводов по данным обследования "
                   "магнитными дефектоскопами, ультразвуковыми дефектоскопами и профилемерами, "
                   "ЗАО 'Нефтегазкомплектсервис', 2000",
  MethodsKBD.GAZNADZOR2008: "Инструкция по оценке дефектов труб... ООО Газнадзор, 2006/2008",
  MethodsKBD.ASMEB31G: "Модифицированный ASME B31G, 1993",
  MethodsKBD.STO112: "СТО Газпром 2-2.3-112",
  MethodsKBD.STO173: "СТО Газпром 2-2.3-173",
  MethodsKBD.ASME2012: "ASME B31G-2012",
  MethodsKBD.GAZNADZOR2013: "Инструкция по оценке дефектов труб... ООО Газнадзор, 2013",
  MethodsKBD.VRD: "ВРД 39-1.10-004-99",

  # Feature
  Feature.ANOMALY: "Аномалия неизвестной природы",
  Feature.NESVAR_STYK: "Несваренный стык патрона",
  Feature.POTERYA_CONTACTA: "Потеря контакта с трубой",
  Feature.EXCENTR_CASE: "Эксцентричный патрон",
  Feature.ANOMAL_KOLTSEVOGO: "Аномалия кольцевого шва",
  Feature.ANOMAL_OBLTSOVKI: "Аномалия облицовки шва",
  Feature.CORROZ_KOLTSEVOGO: "Коррозия на кольцевом шве",
  Feature.NEPROVAR_UTYAZH: "Непровар / утяжина",
  Feature.NO_USILEN_KOLTSEVOGO: "Отсутствие усиления сварного шва",
  Feature.PODKLAD_KOLTSO: "Подкладное кольцо",
  Feature.PODREZ: "Подрез",
  Feature.PRAVKA_KROMOK: "Правка кромок",
  Feature.PROVIS_KORNYA: "Провис корня шва",
  Feature.SMESCHENIE_KROMOK: "Смещение кромок",
  Feature.VNUTRI_SHOV_DEFEKT: "Внутришовный дефект",
  Feature.PODGIB_KROMKY: "Подгиб кромки со смещением",
  Feature.ANOMAL_PRODOLNOGO: "Аномалия продольного шва",
  Feature.VYSHLIFOVKA_PRODOLNOGO: "Место вышлифовки продольного шва",
  Feature.FORMA_PRODOLNOGO: "Нарушение формы продольного шва",
  Feature.ANOMAL_SPIRALNOGO: "Аномалия спирального шва",
  Feature.VYSHLIFOVKA_SPIRALNOGO: "Место вышлифовки спирального шва",
  Feature.FORMA_SPIRALNOGO: "Нарушение формы спирального шва",
  Feature.DENT: "Вмятина",
  Feature.DENT_METAL_LOSS: "Вмятина с дефектами потери металла",
  Feature.VNUTRYSTEN_RASSLOENIE: "Внутристенное расслоение",
  Feature.GOFRA: "Гофра",
  Feature.FACTORY_DEFEKT: "Заводской дефект",
  Feature.METALL_DEFEKT: "Металлургический дефект",
  Feature.VYSHLIFOVKA: "Вышлифовка",
  Feature.ZONE_VERT_CRACKS: "Зона поперечных трещин",
  Feature.ZONE_HOR_CRACKS: "Зона продольных трещин",
  Feature.ZONE_CORROZ: "Зона коррозии",
  Feature.CAVERNA: "Каверна",
  Feature.CORROZ: "Коррозия",
  Feature.KANAVKA_VERT: "Поперечная канавка",
  Feature.METALL_LOSS: "Потеря металла",
  Feature.KANAVKA_HOR: "Продольная канавка",
  Feature.POINT_CORROZ: "Точечная коррозия",
  Feature.MECHANICAL_DEFEKT: "Механическое повреждение",
  Feature.RANDOM_ARC: "Случайная дуга",
  Feature.RASSL_NO_POVERHNOST: "Расслоение с выходом на поверхность",
  Feature.ZAVARKA: "Заварка",
  Feature.ZAVARKA_OTVERST: "Заварка отверстия",
  Feature.TECHNOLOGY_DEFEKT: "Технологический дефект",
  Feature.CRACK_VERT_SHOV: "Трещина на кольцевом шве",
  Feature.CRACK_HOR_SHOV: "Трещина на продольном шве",
  Feature.CRACK_SPIRAL_SHOV: "Трещина на спиральном шве",
  Feature.NESPLOSHNOST_PT: "Несплошность плоскостного типа",
  Feature.CRACK_VERT: "Поперечная трещина",
  Feature.CRACK_HOR: "Продольная трещина",
  Feature.OVAL: "Овализация",
  Feature.METALL_OUT: "Металл снаружи",
  Feature.ISOL_STYK: "Изоляционный стык",
  Feature.CURVE_INSERT: "Кривая вставка",
  Feature.SEGMENT_INSERT: "Сегментная вставка",
  Feature.HOMUT: "Хомут",
  Feature.PIG_RUN: "Камера запуска",
  Feature.PIG_RECEIVE: "Камера приема",
  Feature.MARKER: "Маркер",
  Feature.MARKER_RING: "Маркерное кольцо",
  Feature.MARKER_MAGN: "Маркер магнитный",
  Feature.ZAVAR_BOBYSHKI: "Заварка бобышки",
  Feature.ZAVAR_OKNA: "Заварка окна",
  Feature.REMONT_NAKLAD: "Ремонтная накладка, вышлифовка и т.п.",
  Feature.METALL_CASE_START: "Металлическая упрочняющая муфта, начало",
  Feature.METALL_CASE_END: "Металлическая упрочняющая муфта, конец",
  Feature.KOMPOS_CASE_START: "Композитная упрочняющая муфта, начало",
  Feature.KOMPOS_CASE_END: "Композитная упрочняющая муфта, конец",
  Feature.WRONG_CONSTRUCT: "Недопустимый конструктивный элемент",
  Feature.UNKNOWN: "Нераспознанный объект",
  Feature.DU1000_DU1200: "Переход с диаметра ДУ 1000 мм на ДУ 1200 мм.",
  Feature.DU1200_DU1000: "Переход с диаметра ДУ 1200 мм на ДУ 1000 мм.",
  Feature.DU1200_DU1400: "Переход с диаметра ДУ 1200 мм на ДУ 1400 мм.",
  Feature.DU1400_DU1200: "Переход с диаметра ДУ 1400 мм на ДУ 1200 мм.",
  Feature.TUBE_ARMATURE: "Трубная арматура",
  Feature.ELEMENT_OBUSTROY: "Элемент обустройства",
  Feature.WATER_START: "Начало водной преграды",
  Feature.WATER_END: "Конец водной преграды",
  Feature.FLANETS: "Фланцевые соединения",
  Feature.OTVOD_VREZKA: "Отвод-врезка",
  Feature.CASE_START: "Патрон начало",
  Feature.CASE_END: "Патрон конец",
  Feature.PRIGRUZ_RING: "Пригруз кольцевой",
  Feature.PRIGRUZ_START: "Участок пригрузов начало",
  Feature.PRIGRUZ_END: "Участок пригрузов конец",
  Feature.TROYNIK: "Тройник",
  Feature.WALL_THICK: "Изменение толщины стенки трубы",
  Feature.TURN_START: "Отвод (поворот) начало",
  Feature.TURN_END: "Отвод (поворот) конец",
  Feature.TURN_SEGM_START: "Сегментный участок начало",
  Feature.TURN_SEGM_END: "Сегментный участок конец",
  Feature.TURN_SEGM: "Секторный отвод",
  Feature.WELD: "Шов кольцевой",
  Feature.ZADVIZHKA: "Задвижка",
  Feature.VALVE: "Шаровой кран",

  Feature.LIKVATS: 'Неметалические включения (ликвации)',
  Feature.SEAMEQUAL: 'Смещение заводских (продольных) швов менее 100 мм',
  Feature.NEPROVAR: 'Непровар сварного шва',
  Feature.TEHOKNO: 'Технологическое окно',
  Feature.PITT: 'Язвенная коррозия',
  Feature.PLANE: 'Плоскостной дефект',
}
