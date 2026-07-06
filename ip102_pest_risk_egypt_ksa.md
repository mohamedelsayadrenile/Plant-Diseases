# IP102 Pest Classes — تصنيف خطورة عملي لمصر وKSA
هذا الملف يصنف فئات IP102 إلى 3 مستويات خطورة عملية بالنسبة لاستخدام ReNile في مصر وKSA.

## تعريف مستويات الخطورة
- **طبيعي**: أولوية منخفضة في السوق المصري/الخليجي أو ضرره غالبًا محدود بدون ظروف وبائية.
- **خطر**: قد يسبب خسائر واضحة حسب المحصول والمرحلة والكثافة، ويحتاج متابعة أو تدخل عند الزيادة.
- **شديد الخطورة**: آفة ذات أثر اقتصادي مرتفع، أو تنتشر بسرعة، أو تصيب أجزاء داخلية، أو تنقل أمراضًا، أو تؤثر على التصدير/الجودة.

## ملاحظات تشغيلية
- التصنيف هنا ليس فتوى مكافحة رسمية. هو تصنيف Product/Risk لتحديد أولوية التشخيص داخل النظام.
- بعض أسماء IP102 عامة أو صينية/آسيوية؛ لذلك تم تصنيفها حسب أقرب group زراعي وأثرها المتوقع في مصر/KSA.
- لو ظهر **شديد الخطورة** في المنتج، لا تعتمد على صورة واحدة فقط. اربطه بالمحصول، المرحلة العمرية، الكثافة، والموقع.
- IP102 مناسب كبداية تدريب، لكنه لا يغني عن Dataset محلية من صور ReNile.

## جدول الحشرات والخطورة
| # | IP102 class | مستوى الخطورة | تعريف/سبب الخطورة عند شديد الخطورة |
|---:|---|---|---|
| 1 | `rice leaf roller` | شديد الخطورة | يرقات تتغذى على أوراق الأرز وتلفّها، وقد تسبب فقدًا واضحًا في المسطح الورقي عند الإصابة العالية؛ أهميتها ترتفع في مناطق زراعة الأرز. |
| 2 | `rice leaf caterpillar` | شديد الخطورة | يرقات آكلة للأوراق في الأرز؛ تصبح شديدة الخطورة عند الكثافة العالية لأنها تقلل التمثيل الضوئي وتضعف النمو. |
| 3 | `paddy stem maggot` | خطر |  |
| 4 | `asiatic rice borer` | شديد الخطورة | حفار سيقان الأرز؛ يدخل داخل الساق فيصعب رصده مبكرًا، وقد يسبب موت القمم أو السنابل البيضاء وخسارة إنتاجية. |
| 5 | `yellow rice borer` | شديد الخطورة | حفار مهم في الأرز؛ خطورته في أنه يتغذى داخل الساق ويسبب تلفًا داخليًا لا يظهر بالكامل إلا بعد تقدم الإصابة. |
| 6 | `rice gall midge` | خطر |  |
| 7 | `Rice Stemfly` | خطر |  |
| 8 | `brown plant hopper` | شديد الخطورة | يمتص العصارة من نباتات الأرز وقد يسبب hopper burn، وبعض الأنواع القريبة تنقل أمراضًا فيروسية؛ خطره يزيد مع الكثافات العالية. |
| 9 | `white backed plant hopper` | شديد الخطورة | حشرة ماصة على الأرز؛ تسبب ضعفًا سريعًا للنباتات وقد ترتبط بنقل أمراض فيروسية في نظم الأرز الآسيوية. |
| 10 | `small brown plant hopper` | خطر |  |
| 11 | `rice water weevil` | خطر |  |
| 12 | `rice leafhopper` | خطر |  |
| 13 | `grain spreader thrips` | خطر |  |
| 14 | `rice shell pest` | خطر |  |
| 15 | `grub` | خطر |  |
| 16 | `mole cricket` | خطر |  |
| 17 | `wireworm` | خطر |  |
| 18 | `white margined moth` | طبيعي |  |
| 19 | `black cutworm` | خطر |  |
| 20 | `large cutworm` | خطر |  |
| 21 | `yellow cutworm` | خطر |  |
| 22 | `red spider` | شديد الخطورة | أكاروس/عنكبوت نباتي ماص للعصارة؛ يتكاثر بسرعة في الحرارة والجفاف، ويسبب اصفرارًا وبرونزية وتساقطًا في الأوراق. |
| 23 | `corn borer` | شديد الخطورة | حفار الذرة يدخل داخل الساق أو الكيزان، فيصعب الوصول إليه بالمكافحة بعد الدخول، ويسبب كسرًا وضعفًا وخسارة في المحصول. |
| 24 | `army worm` | شديد الخطورة | يرقات شرهة تتحرك في مجموعات وتلتهم الأوراق بسرعة؛ قد تحول الإصابة من محدودة إلى خسارة كبيرة خلال أيام. |
| 25 | `aphids` | شديد الخطورة | المن حشرات ماصة تتكاثر بسرعة وتفرز عسلية وتشجع العفن الهبابي، وبعض الأنواع تنقل فيروسات نباتية خطيرة. |
| 26 | `Potosiabre vitarsis` | طبيعي |  |
| 27 | `peach borer` | خطر |  |
| 28 | `english grain aphid` | شديد الخطورة | منّ الحبوب؛ يمتص العصارة من القمح والشعير وقد يضعف السنابل وينقل فيروسات في الحبوب. |
| 29 | `green bug` | شديد الخطورة | منّ أخضر على الحبوب؛ يسبب اصفرارًا وحقن سموم نباتية، وقد يكون شديد التأثير على القمح والشعير. |
| 30 | `bird cherry-oataphid` | شديد الخطورة | منّ شائع على الحبوب، خطورته الأساسية في نقل فيروسات مثل barley yellow dwarf في نظم الحبوب. |
| 31 | `wheat blossom midge` | خطر |  |
| 32 | `penthaleus major` | خطر |  |
| 33 | `longlegged spider mite` | شديد الخطورة | أكاروس نباتي قريب من مشاكل العنكبوتيات؛ يمتص العصارة ويتكاثر سريعًا في الظروف الجافة والحارة. |
| 34 | `wheat phloeothrips` | خطر |  |
| 35 | `wheat sawfly` | خطر |  |
| 36 | `cerodonta denticornis` | خطر |  |
| 37 | `beet fly` | خطر |  |
| 38 | `flea beetle` | شديد الخطورة | خنافس صغيرة تقرض الأوراق وتسبب ثقوبًا كثيرة، وخطورتها أعلى على البادرات والنباتات الصغيرة. |
| 39 | `cabbage army worm` | شديد الخطورة | يرقات آكلة للأوراق في الخضروات الصليبية؛ تسبب تآكلًا سريعًا وفقد جودة تسويقية كبير. |
| 40 | `beet army worm` | شديد الخطورة | سبودوبترا متعددة العوائل؛ تصيب خضر ومحاصيل كثيرة، وتسبب تلفًا سريعًا للأوراق والثمار وقد تظهر مقاومة للمبيدات. |
| 41 | `Beet spot flies` | خطر |  |
| 42 | `meadow moth` | خطر |  |
| 43 | `beet weevil` | خطر |  |
| 44 | `sericaorient alismots chulsky` | طبيعي |  |
| 45 | `alfalfa weevil` | خطر |  |
| 46 | `flax budworm` | طبيعي |  |
| 47 | `alfalfa plant bug` | خطر |  |
| 48 | `tarnished plant bug` | خطر |  |
| 49 | `Locustoidea` | خطر |  |
| 50 | `lytta polita` | طبيعي |  |
| 51 | `legume blister beetle` | خطر |  |
| 52 | `blister beetle` | خطر |  |
| 53 | `therioaphis maculata Buckton` | خطر |  |
| 54 | `odontothrips loti` | خطر |  |
| 55 | `Thrips` | شديد الخطورة | التربس حشرات صغيرة ماصة وكاشطة؛ تسبب تشوهات وفضية على الأوراق والثمار، وبعضها ناقل فيروسات، وصعبة الرصد مبكرًا. |
| 56 | `alfalfa seed chalcid` | خطر |  |
| 57 | `Pieris canidia` | خطر |  |
| 58 | `Apolygus lucorum` | خطر |  |
| 59 | `Limacodidae` | خطر |  |
| 60 | `Viteus vitifoliae` | خطر |  |
| 61 | `Colomerus vitis` | خطر |  |
| 62 | `Brevipoalpus lewisi McGregor` | خطر |  |
| 63 | `oides decempunctata` | طبيعي |  |
| 64 | `Polyphagotars onemus latus` | خطر |  |
| 65 | `Pseudococcus comstocki Kuwana` | شديد الخطورة | بق دقيقي يمتص العصارة ويفرز عسلية تؤدي لعفن هبابي؛ خطير في العنب والفاكهة والنباتات المحمية عند انتشاره. |
| 66 | `parathrene regalis` | خطر |  |
| 67 | `Ampelophaga` | خطر |  |
| 68 | `Lycorma delicatula` | خطر |  |
| 69 | `Xylotrechus` | خطر |  |
| 70 | `Cicadella viridis` | خطر |  |
| 71 | `Miridae` | خطر |  |
| 72 | `Trialeurodes vaporariorum` | شديد الخطورة | ذبابة بيضاء greenhouse whitefly؛ تمتص العصارة وتفرز عسلية وتنقل/تساعد على انتشار مشاكل فيروسية وفطرية، وخطيرة في الصوب. |
| 73 | `Erythroneura apicalis` | خطر |  |
| 74 | `Papilio xuthus` | طبيعي |  |
| 75 | `Panonchus citri McGregor` | خطر |  |
| 76 | `Phyllocoptes oleiverus ashmead` | خطر |  |
| 77 | `Icerya purchasi Maskell` | شديد الخطورة | حشرة قشرية/قطنية على الموالح ونباتات زينة؛ تضعف الأشجار وتفرز عسلية وتسبب عفنًا هبابيًا. |
| 78 | `Unaspis yanonensis` | شديد الخطورة | حشرة قشرية على الموالح؛ تسبب ضعفًا وتدهورًا للأفرع والثمار عند الإصابة الشديدة. |
| 79 | `Ceroplastes rubens` | شديد الخطورة | حشرة قشرية شمعية؛ تمتص العصارة وتؤدي للعسلية والعفن الهبابي وضعف النبات، خاصة في الفاكهة والموالح. |
| 80 | `Chrysomphalus aonidum` | شديد الخطورة | حشرة قشرية مدرعة على الموالح؛ تقلل جودة الثمار وتضعف الأشجار، والسيطرة عليها صعبة عند تراكم الأجيال. |
| 81 | `Parlatoria zizyphus Lucus` | شديد الخطورة | حشرة قشرية سوداء على الموالح؛ تسبب تبقع الثمار وضعف النمو وخسائر تسويقية. |
| 82 | `Nipaecoccus vastalor` | شديد الخطورة | بق دقيقي/قريب من mealybugs؛ خطير لأنه ينتشر في تجمعات ويفرز عسلية ويتسبب في عفن هبابي وضعف عام. |
| 83 | `Aleurocanthus spiniferus` | شديد الخطورة | ذبابة بيضاء شوكية على الموالح والشاي؛ تمتص العصارة وتفرز عسلية وتسبب عفنًا هبابيًا كثيفًا. |
| 84 | `Tetradacus c Bactrocera minax` | شديد الخطورة | ذبابة فاكهة/موالح؛ خطيرة لأنها تضع البيض داخل الثمار، فتتلف الثمرة داخليًا وتؤثر على التصدير والحجر الزراعي. |
| 85 | `Dacus dorsalis(Hendel)` | شديد الخطورة | ذبابة فاكهة شرقية؛ آفة حجرية متعددة العوائل، تتلف الثمار من الداخل وتسبب رفضًا تسويقيًا وتصديريًا. |
| 86 | `Bactrocera tsuneonis` | شديد الخطورة | ذبابة فاكهة مرتبطة بالموالح؛ خطورتها في إصابة الثمار داخليًا وصعوبة اكتشاف التلف مبكرًا. |
| 87 | `Prodenia litura` | شديد الخطورة | سبودوبترا/دودة ورقية متعددة العوائل؛ تلتهم الأوراق والثمار وتنتشر سريعًا وقد تكون صعبة المكافحة. |
| 88 | `Adristyrannus` | طبيعي |  |
| 89 | `Phyllocnistis citrella Stainton` | شديد الخطورة | صانعة أنفاق أوراق الموالح؛ اليرقات تحفر داخل نصل الورقة، فتشوه النموات الحديثة وتضعف الشتلات والأشجار الصغيرة. |
| 90 | `Toxoptera citricidus` | شديد الخطورة | منّ الموالح البني؛ شديد الخطورة عالميًا لأنه ناقل فعال لفيروس tristeza في الموالح. |
| 91 | `Toxoptera aurantii` | شديد الخطورة | منّ أسود/بني على الموالح ومحاصيل أخرى؛ يضعف النمو ويفرز عسلية وقد ينقل فيروسات نباتية. |
| 92 | `Aphis citricola Vander Goot` | شديد الخطورة | منّ الموالح/التفاح؛ يهاجم النموات الحديثة ويشوه الأوراق، وقد يساهم في نقل فيروسات. |
| 93 | `Scirtothrips dorsalis Hood` | شديد الخطورة | تربس الفلفل/الفلفل الحار؛ يسبب تشوهات شديدة في النموات والثمار، ويمثل خطرًا عاليًا في الصوب والخضر. |
| 94 | `Dasineura sp` | خطر |  |
| 95 | `Lawana imitata Melichar` | طبيعي |  |
| 96 | `Salurnis marginella Guerr` | طبيعي |  |
| 97 | `Deporaus marginatus Pascoe` | طبيعي |  |
| 98 | `Chlumetia transversa` | طبيعي |  |
| 99 | `Mango flat beak leafhopper` | خطر |  |
| 100 | `Rhytidodera bowrinii white` | طبيعي |  |
| 101 | `Sternochetus frigidus` | شديد الخطورة | سوسة المانجو/البذور؛ تهاجم الثمار والبذور وقد تسبب خسائر حجرية وتسويقية في المانجو. |
| 102 | `Cicadellidae` | شديد الخطورة | نطاطات أوراق متعددة الأنواع؛ تمتص العصارة وبعضها ناقل لأمراض نباتية، وتحتاج تعريفًا أدق للنوع لتقدير الخطر. |

## فئات شديدة الخطورة يجب إعطاؤها أولوية في المنتج
- `rice leaf roller`
- `rice leaf caterpillar`
- `asiatic rice borer`
- `yellow rice borer`
- `brown plant hopper`
- `white backed plant hopper`
- `red spider`
- `corn borer`
- `army worm`
- `aphids`
- `english grain aphid`
- `green bug`
- `bird cherry-oataphid`
- `longlegged spider mite`
- `flea beetle`
- `cabbage army worm`
- `beet army worm`
- `Thrips`
- `Pseudococcus comstocki Kuwana`
- `Trialeurodes vaporariorum`
- `Icerya purchasi Maskell`
- `Unaspis yanonensis`
- `Ceroplastes rubens`
- `Chrysomphalus aonidum`
- `Parlatoria zizyphus Lucus`
- `Nipaecoccus vastalor`
- `Aleurocanthus spiniferus`
- `Tetradacus c Bactrocera minax`
- `Dacus dorsalis(Hendel)`
- `Bactrocera tsuneonis`
- `Prodenia litura`
- `Phyllocnistis citrella Stainton`
- `Toxoptera citricidus`
- `Toxoptera aurantii`
- `Aphis citricola Vander Goot`
- `Scirtothrips dorsalis Hood`
- `Sternochetus frigidus`
- `Cicadellidae`

## Mapping مقترح لفئات محلية غير مغطاة جيدًا في IP102
| Pest محلي مهم | هل موجود في IP102؟ | الإجراء |
|---|---|---|
| Bemisia tabaci | غير موجود بالاسم، قريب من Trialeurodes vaporariorum | اجمع صور محلية ودرّب class منفصل |
| Tuta absoluta | غير موجودة بشكل مباشر | لازم Dataset محلية/خارجية منفصلة |
| Tetranychus urticae | قريب من red spider/spider mite classes | اجمع صور محلية لفصل النوع |
| Thrips tabaci | موجود كـ Thrips عام/قريب | Fine-tune على صور صوب مصر/KSA |
| Frankliniella occidentalis | غير مغطى بوضوح | أضف class منفصل |
| Liriomyza trifolii | غير مغطى بوضوح | أضف adult + damage classes |
| Spodoptera littoralis | قريب من armyworm/Prodenia litura | أضف class محلي |
| Phenacoccus hirsutus | قريب من mealybug classes | أضف class محلي |

## مصادر
- IP102: A Large-Scale Benchmark Dataset for Insect Pest Recognition — CVPR 2019.
- IP102 GitHub repository and classes.txt.
- دراسات مصرية عن آفات الطماطم والخضر تشمل aphids, Thrips tabaci, Bemisia tabaci, Tuta absoluta, Phenacoccus hirsutus, Tetranychus urticae.
