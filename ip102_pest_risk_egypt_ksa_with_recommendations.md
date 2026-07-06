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


## سياسة توصيات الرش المؤقتة
- التوصيات التالية هي **مواد فعالة** وليست أسماء منتجات تجارية.
- لا يتم عرض جرعة أو عدد رشات داخل المنتج قبل ربطها بالمحصول، الدولة، التسجيل المحلي، وفترة الأمان PHI.
- أي توصية يجب أن تظهر للمستخدم بهذه الصيغة: **مادة فعالة محتملة + الالتزام بملصق المبيد المحلي والمهندس الزراعي**.
- يجب تدوير المواد الفعالة حسب IRAC Mode of Action لتقليل المقاومة، خصوصًا مع whitefly, thrips, mites, Tuta/armyworms, aphids.
- لو الحشرة مصنفة **طبيعي** لا تظهر توصية رش افتراضية؛ اكتفِ بالمتابعة أو طلب صورة أوضح.

## جدول الحشرات والخطورة
| # | IP102 class | مستوى الخطورة | توصية مادة فعالة مؤقتة | تعريف/سبب الخطورة عند شديد الخطورة |
|---:|---|---|---|---|
| 1 | `rice leaf roller` | شديد الخطورة | Chlorantraniliprole أو Cartap أو Emamectin benzoate | يرقات تتغذى على أوراق الأرز وتلفّها، وقد تسبب فقدًا واضحًا في المسطح الورقي عند الإصابة العالية؛ أهميتها ترتفع في مناطق زراعة الأرز. |
| 2 | `rice leaf caterpillar` | شديد الخطورة | Chlorantraniliprole أو Cartap أو Emamectin benzoate | يرقات آكلة للأوراق في الأرز؛ تصبح شديدة الخطورة عند الكثافة العالية لأنها تقلل التمثيل الضوئي وتضعف النمو. |
| 3 | `paddy stem maggot` | خطر | Chlorantraniliprole أو Cartap أو Emamectin benzoate |  |
| 4 | `asiatic rice borer` | شديد الخطورة | Chlorantraniliprole أو Emamectin benzoate | حفار سيقان الأرز؛ يدخل داخل الساق فيصعب رصده مبكرًا، وقد يسبب موت القمم أو السنابل البيضاء وخسارة إنتاجية. |
| 5 | `yellow rice borer` | شديد الخطورة | Chlorantraniliprole أو Emamectin benzoate | حفار مهم في الأرز؛ خطورته في أنه يتغذى داخل الساق ويسبب تلفًا داخليًا لا يظهر بالكامل إلا بعد تقدم الإصابة. |
| 6 | `rice gall midge` | خطر | Chlorantraniliprole أو Cartap أو Emamectin benzoate |  |
| 7 | `Rice Stemfly` | خطر | Chlorantraniliprole أو Cartap أو Emamectin benzoate |  |
| 8 | `brown plant hopper` | شديد الخطورة | Buprofezin أو Pymetrozine أو Acetamiprid | يمتص العصارة من نباتات الأرز وقد يسبب hopper burn، وبعض الأنواع القريبة تنقل أمراضًا فيروسية؛ خطره يزيد مع الكثافات العالية. |
| 9 | `white backed plant hopper` | شديد الخطورة | Buprofezin أو Pymetrozine أو Acetamiprid | حشرة ماصة على الأرز؛ تسبب ضعفًا سريعًا للنباتات وقد ترتبط بنقل أمراض فيروسية في نظم الأرز الآسيوية. |
| 10 | `small brown plant hopper` | خطر | Buprofezin أو Pymetrozine أو Acetamiprid |  |
| 11 | `rice water weevil` | خطر | Chlorantraniliprole أو Cartap أو Emamectin benzoate |  |
| 12 | `rice leafhopper` | خطر | Buprofezin أو Pymetrozine أو Acetamiprid |  |
| 13 | `grain spreader thrips` | خطر | Spinosad أو Spinetoram أو Abamectin |  |
| 14 | `rice shell pest` | خطر | Chlorantraniliprole أو Cartap أو Emamectin benzoate |  |
| 15 | `grub` | خطر | Chlorantraniliprole أو Tefluthrin/مادة تربة مسجلة |  |
| 16 | `mole cricket` | خطر | Chlorantraniliprole أو Tefluthrin/مادة تربة مسجلة |  |
| 17 | `wireworm` | خطر | Chlorantraniliprole أو Tefluthrin/مادة تربة مسجلة |  |
| 18 | `white margined moth` | طبيعي |  |  |
| 19 | `black cutworm` | خطر | Indoxacarb أو Chlorantraniliprole أو Lambda-cyhalothrin |  |
| 20 | `large cutworm` | خطر | Indoxacarb أو Chlorantraniliprole أو Lambda-cyhalothrin |  |
| 21 | `yellow cutworm` | خطر | Indoxacarb أو Chlorantraniliprole أو Lambda-cyhalothrin |  |
| 22 | `red spider` | شديد الخطورة | Abamectin أو Bifenazate أو Spiromesifen | أكاروس/عنكبوت نباتي ماص للعصارة؛ يتكاثر بسرعة في الحرارة والجفاف، ويسبب اصفرارًا وبرونزية وتساقطًا في الأوراق. |
| 23 | `corn borer` | شديد الخطورة | Chlorantraniliprole أو Emamectin benzoate | حفار الذرة يدخل داخل الساق أو الكيزان، فيصعب الوصول إليه بالمكافحة بعد الدخول، ويسبب كسرًا وضعفًا وخسارة في المحصول. |
| 24 | `army worm` | شديد الخطورة | Emamectin benzoate أو Chlorantraniliprole أو Indoxacarb | يرقات شرهة تتحرك في مجموعات وتلتهم الأوراق بسرعة؛ قد تحول الإصابة من محدودة إلى خسارة كبيرة خلال أيام. |
| 25 | `aphids` | شديد الخطورة | Flonicamid أو Pirimicarb أو Acetamiprid | المن حشرات ماصة تتكاثر بسرعة وتفرز عسلية وتشجع العفن الهبابي، وبعض الأنواع تنقل فيروسات نباتية خطيرة. |
| 26 | `Potosiabre vitarsis` | طبيعي |  |  |
| 27 | `peach borer` | خطر | Chlorantraniliprole أو Emamectin benzoate |  |
| 28 | `english grain aphid` | شديد الخطورة | Flonicamid أو Pirimicarb أو Acetamiprid | منّ الحبوب؛ يمتص العصارة من القمح والشعير وقد يضعف السنابل وينقل فيروسات في الحبوب. |
| 29 | `green bug` | شديد الخطورة | Flonicamid أو Pirimicarb أو Acetamiprid | منّ أخضر على الحبوب؛ يسبب اصفرارًا وحقن سموم نباتية، وقد يكون شديد التأثير على القمح والشعير. |
| 30 | `bird cherry-oataphid` | شديد الخطورة | Flonicamid أو Pirimicarb أو Acetamiprid | منّ شائع على الحبوب، خطورته الأساسية في نقل فيروسات مثل barley yellow dwarf في نظم الحبوب. |
| 31 | `wheat blossom midge` | خطر | Cyromazine أو Spinosad أو Lambda-cyhalothrin حسب نوع اليرقة/الحشرة |  |
| 32 | `penthaleus major` | خطر | Abamectin أو Bifenazate أو Spiromesifen |  |
| 33 | `longlegged spider mite` | شديد الخطورة | Abamectin أو Bifenazate أو Spiromesifen | أكاروس نباتي قريب من مشاكل العنكبوتيات؛ يمتص العصارة ويتكاثر سريعًا في الظروف الجافة والحارة. |
| 34 | `wheat phloeothrips` | خطر | Spinosad أو Spinetoram أو Abamectin |  |
| 35 | `wheat sawfly` | خطر | Cyromazine أو Spinosad أو Lambda-cyhalothrin حسب نوع اليرقة/الحشرة |  |
| 36 | `cerodonta denticornis` | خطر | Abamectin أو Cyromazine أو Spinosad |  |
| 37 | `beet fly` | خطر | Cyromazine أو Spinosad أو Lambda-cyhalothrin حسب نوع اليرقة/الحشرة |  |
| 38 | `flea beetle` | شديد الخطورة | Acetamiprid أو Lambda-cyhalothrin أو Deltamethrin | خنافس صغيرة تقرض الأوراق وتسبب ثقوبًا كثيرة، وخطورتها أعلى على البادرات والنباتات الصغيرة. |
| 39 | `cabbage army worm` | شديد الخطورة | Emamectin benzoate أو Chlorantraniliprole أو Indoxacarb | يرقات آكلة للأوراق في الخضروات الصليبية؛ تسبب تآكلًا سريعًا وفقد جودة تسويقية كبير. |
| 40 | `beet army worm` | شديد الخطورة | Emamectin benzoate أو Chlorantraniliprole أو Indoxacarb | سبودوبترا متعددة العوائل؛ تصيب خضر ومحاصيل كثيرة، وتسبب تلفًا سريعًا للأوراق والثمار وقد تظهر مقاومة للمبيدات. |
| 41 | `Beet spot flies` | خطر | مادة فعالة مسجلة حسب المحصول: Acetamiprid أو Lambda-cyhalothrin كاختيار مبدئي فقط |  |
| 42 | `meadow moth` | خطر | Emamectin benzoate أو Chlorantraniliprole أو Spinosad |  |
| 43 | `beet weevil` | خطر | Acetamiprid أو Lambda-cyhalothrin أو Chlorantraniliprole |  |
| 44 | `sericaorient alismots chulsky` | طبيعي |  |  |
| 45 | `alfalfa weevil` | خطر | Acetamiprid أو Lambda-cyhalothrin أو Chlorantraniliprole |  |
| 46 | `flax budworm` | طبيعي |  |  |
| 47 | `alfalfa plant bug` | خطر | Acetamiprid أو Flonicamid أو Lambda-cyhalothrin |  |
| 48 | `tarnished plant bug` | خطر | Acetamiprid أو Flonicamid أو Lambda-cyhalothrin |  |
| 49 | `Locustoidea` | خطر | Lambda-cyhalothrin أو Deltamethrin |  |
| 50 | `lytta polita` | طبيعي |  |  |
| 51 | `legume blister beetle` | خطر | Acetamiprid أو Lambda-cyhalothrin أو Deltamethrin |  |
| 52 | `blister beetle` | خطر | Acetamiprid أو Lambda-cyhalothrin أو Deltamethrin |  |
| 53 | `therioaphis maculata Buckton` | خطر | Flonicamid أو Pirimicarb أو Acetamiprid |  |
| 54 | `odontothrips loti` | خطر | Spinosad أو Spinetoram أو Abamectin |  |
| 55 | `Thrips` | شديد الخطورة | Spinosad أو Spinetoram أو Abamectin | التربس حشرات صغيرة ماصة وكاشطة؛ تسبب تشوهات وفضية على الأوراق والثمار، وبعضها ناقل فيروسات، وصعبة الرصد مبكرًا. |
| 56 | `alfalfa seed chalcid` | خطر | Lambda-cyhalothrin أو Acetamiprid |  |
| 57 | `Pieris canidia` | خطر | Emamectin benzoate أو Chlorantraniliprole أو Spinosad |  |
| 58 | `Apolygus lucorum` | خطر | Acetamiprid أو Flonicamid أو Lambda-cyhalothrin |  |
| 59 | `Limacodidae` | خطر | Emamectin benzoate أو Chlorantraniliprole أو Spinosad |  |
| 60 | `Viteus vitifoliae` | خطر | مادة فعالة مسجلة حسب المحصول: Acetamiprid أو Lambda-cyhalothrin كاختيار مبدئي فقط |  |
| 61 | `Colomerus vitis` | خطر | Abamectin أو Bifenazate أو Spiromesifen |  |
| 62 | `Brevipoalpus lewisi McGregor` | خطر | Abamectin أو Bifenazate أو Spiromesifen |  |
| 63 | `oides decempunctata` | طبيعي |  |  |
| 64 | `Polyphagotars onemus latus` | خطر | Abamectin أو Bifenazate أو Spiromesifen |  |
| 65 | `Pseudococcus comstocki Kuwana` | شديد الخطورة | Spirotetramat أو Acetamiprid + زيت معدني | بق دقيقي يمتص العصارة ويفرز عسلية تؤدي لعفن هبابي؛ خطير في العنب والفاكهة والنباتات المحمية عند انتشاره. |
| 66 | `parathrene regalis` | خطر | Chlorantraniliprole أو Emamectin benzoate |  |
| 67 | `Ampelophaga` | خطر | Emamectin benzoate أو Chlorantraniliprole أو Spinosad |  |
| 68 | `Lycorma delicatula` | خطر | مادة فعالة مسجلة حسب المحصول: Acetamiprid أو Lambda-cyhalothrin كاختيار مبدئي فقط |  |
| 69 | `Xylotrechus` | خطر | Chlorantraniliprole أو Emamectin benzoate |  |
| 70 | `Cicadella viridis` | خطر | Buprofezin أو Pymetrozine أو Acetamiprid |  |
| 71 | `Miridae` | خطر | Acetamiprid أو Flonicamid أو Lambda-cyhalothrin |  |
| 72 | `Trialeurodes vaporariorum` | شديد الخطورة | Pyriproxyfen أو Buprofezin أو Spirotetramat أو Cyantraniliprole | ذبابة بيضاء greenhouse whitefly؛ تمتص العصارة وتفرز عسلية وتنقل/تساعد على انتشار مشاكل فيروسية وفطرية، وخطيرة في الصوب. |
| 73 | `Erythroneura apicalis` | خطر | مادة فعالة مسجلة حسب المحصول: Acetamiprid أو Lambda-cyhalothrin كاختيار مبدئي فقط |  |
| 74 | `Papilio xuthus` | طبيعي |  |  |
| 75 | `Panonchus citri McGregor` | خطر | Abamectin أو Bifenazate أو Spiromesifen |  |
| 76 | `Phyllocoptes oleiverus ashmead` | خطر | Abamectin أو Bifenazate أو Spiromesifen |  |
| 77 | `Icerya purchasi Maskell` | شديد الخطورة | Spirotetramat أو Acetamiprid + زيت معدني | حشرة قشرية/قطنية على الموالح ونباتات زينة؛ تضعف الأشجار وتفرز عسلية وتسبب عفنًا هبابيًا. |
| 78 | `Unaspis yanonensis` | شديد الخطورة | زيت معدني + Pyriproxyfen أو Spirotetramat | حشرة قشرية على الموالح؛ تسبب ضعفًا وتدهورًا للأفرع والثمار عند الإصابة الشديدة. |
| 79 | `Ceroplastes rubens` | شديد الخطورة | زيت معدني + Pyriproxyfen أو Spirotetramat | حشرة قشرية شمعية؛ تمتص العصارة وتؤدي للعسلية والعفن الهبابي وضعف النبات، خاصة في الفاكهة والموالح. |
| 80 | `Chrysomphalus aonidum` | شديد الخطورة | زيت معدني + Pyriproxyfen أو Spirotetramat | حشرة قشرية مدرعة على الموالح؛ تقلل جودة الثمار وتضعف الأشجار، والسيطرة عليها صعبة عند تراكم الأجيال. |
| 81 | `Parlatoria zizyphus Lucus` | شديد الخطورة | زيت معدني + Pyriproxyfen أو Spirotetramat | حشرة قشرية سوداء على الموالح؛ تسبب تبقع الثمار وضعف النمو وخسائر تسويقية. |
| 82 | `Nipaecoccus vastalor` | شديد الخطورة | Spirotetramat أو Acetamiprid + زيت معدني | بق دقيقي/قريب من mealybugs؛ خطير لأنه ينتشر في تجمعات ويفرز عسلية ويتسبب في عفن هبابي وضعف عام. |
| 83 | `Aleurocanthus spiniferus` | شديد الخطورة | Pyriproxyfen أو Buprofezin أو Spirotetramat أو Cyantraniliprole | ذبابة بيضاء شوكية على الموالح والشاي؛ تمتص العصارة وتفرز عسلية وتسبب عفنًا هبابيًا كثيفًا. |
| 84 | `Tetradacus c Bactrocera minax` | شديد الخطورة | Spinosad bait أو Protein bait + مادة مسجلة لذبابة الفاكهة | ذبابة فاكهة/موالح؛ خطيرة لأنها تضع البيض داخل الثمار، فتتلف الثمرة داخليًا وتؤثر على التصدير والحجر الزراعي. |
| 85 | `Dacus dorsalis(Hendel)` | شديد الخطورة | Spinosad bait أو Protein bait + مادة مسجلة لذبابة الفاكهة | ذبابة فاكهة شرقية؛ آفة حجرية متعددة العوائل، تتلف الثمار من الداخل وتسبب رفضًا تسويقيًا وتصديريًا. |
| 86 | `Bactrocera tsuneonis` | شديد الخطورة | Spinosad bait أو Protein bait + مادة مسجلة لذبابة الفاكهة | ذبابة فاكهة مرتبطة بالموالح؛ خطورتها في إصابة الثمار داخليًا وصعوبة اكتشاف التلف مبكرًا. |
| 87 | `Prodenia litura` | شديد الخطورة | Emamectin benzoate أو Chlorantraniliprole أو Indoxacarb | سبودوبترا/دودة ورقية متعددة العوائل؛ تلتهم الأوراق والثمار وتنتشر سريعًا وقد تكون صعبة المكافحة. |
| 88 | `Adristyrannus` | طبيعي |  |  |
| 89 | `Phyllocnistis citrella Stainton` | شديد الخطورة | Abamectin أو Cyromazine أو Spinosad | صانعة أنفاق أوراق الموالح؛ اليرقات تحفر داخل نصل الورقة، فتشوه النموات الحديثة وتضعف الشتلات والأشجار الصغيرة. |
| 90 | `Toxoptera citricidus` | شديد الخطورة | Flonicamid أو Pirimicarb أو Acetamiprid | منّ الموالح البني؛ شديد الخطورة عالميًا لأنه ناقل فعال لفيروس tristeza في الموالح. |
| 91 | `Toxoptera aurantii` | شديد الخطورة | Flonicamid أو Pirimicarb أو Acetamiprid | منّ أسود/بني على الموالح ومحاصيل أخرى؛ يضعف النمو ويفرز عسلية وقد ينقل فيروسات نباتية. |
| 92 | `Aphis citricola Vander Goot` | شديد الخطورة | Flonicamid أو Pirimicarb أو Acetamiprid | منّ الموالح/التفاح؛ يهاجم النموات الحديثة ويشوه الأوراق، وقد يساهم في نقل فيروسات. |
| 93 | `Scirtothrips dorsalis Hood` | شديد الخطورة | Spinosad أو Spinetoram أو Abamectin | تربس الفلفل/الفلفل الحار؛ يسبب تشوهات شديدة في النموات والثمار، ويمثل خطرًا عاليًا في الصوب والخضر. |
| 94 | `Dasineura sp` | خطر | Cyromazine أو Spinosad أو Lambda-cyhalothrin حسب نوع اليرقة/الحشرة |  |
| 95 | `Lawana imitata Melichar` | طبيعي |  |  |
| 96 | `Salurnis marginella Guerr` | طبيعي |  |  |
| 97 | `Deporaus marginatus Pascoe` | طبيعي |  |  |
| 98 | `Chlumetia transversa` | طبيعي |  |  |
| 99 | `Mango flat beak leafhopper` | خطر | Buprofezin أو Pymetrozine أو Acetamiprid |  |
| 100 | `Rhytidodera bowrinii white` | طبيعي |  |  |
| 101 | `Sternochetus frigidus` | شديد الخطورة | Chlorantraniliprole أو Emamectin benzoate | سوسة المانجو/البذور؛ تهاجم الثمار والبذور وقد تسبب خسائر حجرية وتسويقية في المانجو. |
| 102 | `Cicadellidae` | شديد الخطورة | Buprofezin أو Pymetrozine أو Acetamiprid | نطاطات أوراق متعددة الأنواع؛ تمتص العصارة وبعضها ناقل لأمراض نباتية، وتحتاج تعريفًا أدق للنوع لتقدير الخطر. |

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
- IRAC Mode of Action Classification Scheme لاستخدام تدوير المواد الفعالة وتقليل المقاومة.
- FAO/WHO pesticide labelling guidance: الالتزام بالتسجيل المحلي، الجرعة، فترة الأمان PHI، وفترة إعادة الدخول REI حسب الملصق.
