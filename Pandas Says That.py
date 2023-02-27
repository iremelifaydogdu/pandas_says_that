#Python ile Veri Analizi

#Pandas


#Veri manipülasyonu ve veri analizi için
#Pandas Series:Tek boyutlu pandas dataframe'i
#Veri Okuma
#Veriye hızlı bir bakış
#Toplulaştırma ve gruplama
#Apply ve lambda
#Birleştirme (join) işlemleri

#Pandas Serileri: Tek boyutlu ve index bilgisi barındıran bir veri tipidir.
#Pandas serileri hk. : Farkında olmak ve gerektiğinde veri tpleri arasında geçiş yapabiliyor olmak bzim için önemlidir.

#Veri manipülasyonu ve veri analizi işlemlerimizi daha çok pandas dataframe'i üzerinden gerçekleştiriyor olacağız.
 import pandas as pd
#pd.Series #Bu bir methodtur. Bana bir liste ya da faklı bir tipte veri ver ki ben bunu panas serisine dönüştürebileyim.
pd.Series([10, 77,  12, 4, 5])
#index bilgisi zamana bağlılıktan dolayı ortaya çıkmıştır. Ekonometri bilgileri için.
s=pd.Series([10, 77,  12, 4, 5])
type(s)
#>pandas.core.series.Series
#Veri yapıları bizim için şu açıdan değerlidir: Fonksiyonların bizden beklediği ihtiyaçları daha doğru bir şekilde yerine getirebilme imkanı sağlar.
#Fonksiyonların beklentileri karşılanmadığı durumlarda hata alırız.
s.index
#> RangeIndex(start=0, stop=5, step=1)
s.dtype
# dtype('int64')
s.size
#5
s.ndim
#1
s.values
#>array([10, 77, 12,  4,  5], dtype=int64)
type(s.values)
#numpy.ndarray
#s.values değerlerini istemek indeks bilgisiyle ilgilenmiyorum demektir.
s.head()
s.tail()

#Veri okuma: Dış kaynaklı verileri okuma hakkında konuşacağız bu bölümde.
df=pd.read_csv("HAFTA 2/persona.csv")
df.head()

#Veriye Hızlı Bakış: Elimize bir pandas dataframe'i geldiğinde hızlı bir şekilde hangi methodları uygulayabiliriz burada ondan bahsedeceğiz.:

import seaborn as sns #burada seaborn içinde bulunan bir datasetten yararlnacağımız için kütüpaneyi çekiyorz.
df=sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
#RangeIndex(start=0, stop=891, step=1)
df.describe().T #Hızlı bir şekilde özet istatistiklerine (betimsel istatistikleri) erişmek istersek
df.isnull().values.any()#eksik değer var mı
#True
df.isnull() #True falselardan oluşan bir çıktı döner.
df.isnull().values
#array([[False, False, False, ..., False, False, False],
#       [False, False, False, ..., False, False, False],
 #      [False, False, False, ..., False, False, False],
  #     ...,
   #    [False, False, False, ..., False, False, False],
    #   [False, False, False, ..., False, False, False],
     #  [False, False, False, ..., False, False, False]])

df.isnull().sum() #değişkenlerdeki eksiklik durumu gözlenmek isterse
#survived         0
#pclass           0
#sex              0
#age            177
#sibsp            0
#parch            0
#fare             0
#embarked         2
#class            0
#who              0
#adult_male       0
#deck           688
#embark_town      2
#alive            0
#alone            0
#dtype: int64
df["sex"].head()
df["sex"].value_counts() #Bu kategorik değişkenin sınıfları ve bunlardan kaçar tane var olduğu bilgisi gelri.
#male      577
#female    314
#Name: sex, dtype: int64


#Pandas'ta Seçim İşlemleri

import pandas as pd
import seaborn as sns
df=sns.load_dataset("titanic")
df.head()

df.index
df[0:13] #dilimleme, slice işlemi için
#indekslerde silme işlemi:
df.drop(0,axis=0).head() #kalıcı şekilde silmez
#Birden fazla satırı(indexi) silme işlemi için: Fancy index kavramıyla silme

delete_indexes=[1,3,5,7]
df.drop(delete_indexes,axis=0).head()

#Kalıcı şekilde olması için:
#df=df.drop(delete_indexes,axis=0).head()
#df.drop(delete_indexes,axis=0,inplace=True).head()

#Değişkeni İndexe Çevirmek:
#Aşağıdakilerden ikisi de seçim işlemi için kullanılır.
df["age"].head()
df.age.head()

#Yaş değişkenini indexe atmak istiyorum.
df.index=df["age"]
df.index
#Float64Index([22.0, 38.0, 26.0, 35.0, 35.0,  nan, 54.0,  2.0, 27.0, 14.0,
#              ...
 #             33.0, 22.0, 28.0, 25.0, 39.0, 27.0, 19.0,  nan, 26.0, 32.0],
  #           dtype='float64', name='age', length=891)
#Yaş bilgisi bir değişken olarak index e eklenmiş oldu

#Madem indeks olarak ekledik Artık değişken olarak ihtiyacımız yok
df.drop("age", axis=1).head()
df.drop("age", axis=1,inplace=True) #KAlıcı olarak bu dataframeden gitti.


#Indexi değişkene çevirmek
#Şimdi bu şekilde bir indexi değişkene çevirmek istersek ne yapıcaz görelim:
df.index
#df["age"]:Hata alır çünkü sildik
#1.YOL
df["age"]= df.index #df["age"] yazıp df.index'e eşitlersek değişken olarak var mı yok mu bakar yoksa atar.
df.head() #yaş değişkeninin eklendiğini görürüz.
#2.YOL:reset_index fonksiyonu
df.drop("age", axis=1,inplace=True) #önce yukarı da eklemiştik onu bi silelim ki hata almasın aşağıdaki kodumuz.

df.reset_index().head()
df=df.reset_index()
df.head()

#Değişkenler Üzerinde İşlemler
#Satır indeksilerinde çalıştık şimdi sütun indeksleri diyebileceğimiz yani değişkenler üzerinde işlemler gerçekleştireceğiz.

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None) #gösterilecek olan maksimum kolon sayısı olmasın yani her kolonu göster diyoruz.
df=sns.load_dataset("titanic")
df.head()

#Bir dataframede herhangibir değişkenin varlığını sorgulamak için :
"age" in df
#True

#Özelilikle bir değişken seçmek istersek:
df["age"].head()
df.age.head()


#Tek bir değişken seçerken seçimin sonucu pandas serisi olur:
df["age"].head()
type(df["age"].head())
#>pandas.core.series.Series

#Tek bir değişken seçerken seçimin sncunun dataframe olarak kalmasını istiyorsanız
#iki köşeli parantez kullanarak seçim yapmanız gerekir.
df[["age"]].head()
type(df[["age"]].head())
#> pandas.core.frame.DataFrame

df[["age", "alive"]] #birden fazla değişken seçmek için

#elimizde daha fazla değişken varsa:

col_names= ["age", "adult_male", "alive"] #fancy index kavramı
df[col_names]

#Dataframe'e yeni bir değişken ekleme kavramı

df["age2"]=df["age"]**2
df["age3"]=df["age"]/df["age2"]
df.head()

#Değişken silme işlemi için ne yapabiliriz:
df.drop("age3", axis=1).head()
df.drop(col_names, axis=1).head()

#Bir veri setinde belirli bir string ifadeyi barındıran ifadeleri silmek için ne yapabilirim
df.loc[:, df.columns.str.contains("age")].head()
#loc label based seçim yapmak için kullanılır.
#Bu dataframein kolonlarındaki değişkenlere bir string operasyonu yapıcam. contains methodunu kullanıyorum.
#contains methodu der ki bana bir string ifade ver ben benden önceki stringde bu var mı yok mu arayayım
#yaş ifadesi aradı ve yaş ifadesi geçenleri seçti.

#silmek için de tilda koyucaz:
df.loc[:, ~df.columns.str.contains("age")].head()
#loc dataframelerde seçme işlemi uygulamak için kullanılan bir diğer özel yapıdır.

#Loc & Iloc
#Dataframelerde seçim işlemi yapmak için kullanılan özel yapılardır.


import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None) #gösterilecek olan maksimum kolon sayısı olmasın yani her kolonu göster diyoruz.
df=sns.load_dataset("titanic")
df.head()

#iloc: integer based selection: klasik indeks bilgisi vererek seçim yapma işlemlerini ifade eder.
#loc: mutlak olarak indekslerdeki labellara göre seçim yapar.

df.iloc[0:3] #0'dan 3'E KADAR
df.iloc[0,0]

#loc: label based selection

df.loc[0:3] #0 ve 3 ve arasındakilerin hepsini seçer. mutlak olarak isimlendirmenin kendisini seçer.

#hata alıcak yapı: df.iloc[0:3,"age"]
df.loc[0:3,"age"]
#0    22.0
#1    38.0
#2    26.0
#3    35.0
#Name: age, dtype: float64

#Koşullu seçim (Conditional Selection)
#Dataframe'lerde koşullu işlemleri sağlayacağız.

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None) #gösterilecek olan maksimum kolon sayısı olmasın yani her kolonu göster diyoruz.
df=sns.load_dataset("titanic")
df.head()

#df[] : ey dataframe ben geliyorm seçim yapacağım :)
#seçim yapacaksan 1. bana bir koşul gir ve bu koşulu girerken bu koşulun hangi değişkene uygulanacağı bilgisini de gir.
df[df["age"]>50].head()
df[df["age"]>50].count() #yaşı 50'den büyük olan kaç kişi var, değişken seçmediğimiz için hepsine count atacak.
#survived       64
#pclass         64
#sex            64
#age            64
#sibsp          64
#parch          64
##fare           64
#embarked       63
#class          64
#who            64
#adult_male     64
#deck           33
#embark_town    63
#alive          64
#alone          64
#dtype: int64
df[df["age"]>50]["age"].count()
#> 64

#yaşı 50'den büyük olan kişilerin class değerlerini merak ediyoruz diyelim. elimizde koşul var ve bir değişken seçme motivasyonumuz var ise:
df.loc[df["age"]>50, "class"].head()
#>6      First
#11     First
#15    Second
#33    Second
#54     First
#Name: class, dtype: category
#Categories (3, object): ['First', 'Second', 'Third']

df.loc[df["age"]>50, ["class", "age"]].head()
#     class   age
#6    First  54.0
#11   First  58.0
#15  Second  55.0
#33  Second  66.0
#54   First  65.0

#Yaşı 50'den büyük olan erkekleri seçmek istiyoruz diyelim: 1 koşulu anladık ama 2 koulu nasıl giricez
#hem yaşı 50den büyük hem cinsiyeti erkek
#birden fazla koşul giriliyorsa birden fazla koşul parantez içersine alınması gerekir.

df.loc[(df["age"]>50) & (df["sex"]=="male"), ["class", "age"]].head()
#     class   age
#6    First  54.0
#33  Second  66.0
#54   First  65.0
#94   Third  59.0
#96   First  71.0

#bu dataframe'e bir koşul daha eklemek istiyoruz diyelim:
df.loc[(df["age"] > 50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg"), ["class", "age", "embark_town"]].head()
#     class   age embark_town
#54   First  65.0   Cherbourg
#96   First  71.0   Cherbourg
#155  First  51.0   Cherbourg
#174  First  56.0   Cherbourg
#487  First  58.0   Cherbourg

#tOPLULAŞTIRMA VE GRUPLAMA

#count()
#first()
#last()
#mean()
#median()
#min()
#max()
#std()
#var()
#pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None) #gösterilecek olan maksimum kolon sayısı olmasın yani her kolonu göster diyoruz.
df=sns.load_dataset("titanic")
df.head()


df["age"].mean()
#>29.69911764705882

df.groupby("sex")["age"].mean()
#>sex
#female    27.915709
#male      30.726645
#Name: age, dtype: float64


df.groupby("sex").agg({"age": "mean"})
#              age
#sex
#female  27.915709
#male    30.726645


df.groupby("sex").agg({"age": ["mean", "sum"]})
#>              age
#             mean       sum
#sex
#female  27.915709   7286.00
#male    30.726645  13919.17



df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})
#>              age            survived
#             mean       sum      mean
#sex
#female  27.915709   7286.00  0.742038
#male    30.726645  13919.17  0.188908




df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})
#                          age  survived
#                         mean      mean
#sex    embark_town
#female Cherbourg    28.344262  0.876712
#       Queenstown   24.291667  0.750000
 #      Southampton  27.771505  0.689655
#male   Cherbourg    32.998841  0.305263
#       Queenstown   30.937500  0.073171
#       Southampton  30.291440  0.174603




df.groupby(["sex", "embark_town"]).agg({
       "age": ["mean"],
       "survived": "mean",
        "sex": "count"})
#>                          age  survived   sex
#                         mean      mean count
#sex    embark_town
#female Cherbourg    28.344262  0.876712    73
#       Queenstown   24.291667  0.750000    36
#       Southampton  27.771505  0.689655   203
#male   Cherbourg    32.998841  0.305263    95
#       Queenstown   30.937500  0.073171    41
#       Southampton  30.291440  0.174603   441

#Pivot Table
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None) #gösterilecek olan maksimum kolon sayısı olmasın yani her kolonu göster diyoruz.
df=sns.load_dataset("titanic")
df.head()


df.pivot_table("survived", "sex", "embarked")
#embarked         C         Q         S
#sex
#female    0.876712  0.750000  0.689655
#male      0.305263  0.073171  0.174603

df.pivot_table("survived", "sex", "embarked", aggfunc="std")
#embarked         C         Q         S
#sex
#female    0.331042  0.439155  0.463778
#male      0.462962  0.263652  0.380058

df.pivot_table("survived", "sex", ["embarked", "class"])
#embarked         C                      Q                          S  \
#class        First Second     Third First Second     Third     First
#sex
#female    0.976744    1.0  0.652174   1.0    1.0  0.727273  0.958333
#male      0.404762    0.2  0.232558   0.0    0.0  0.076923  0.354430
#embarked
#class       Second     Third
#sex
#female    0.910448  0.375000
#male      0.154639  0.128302

df["new_age"]=pd.cut(df["age"], [0,10,18,25,40,90])

df.pivot_table("survived", "sex", "new_age")
#>new_age   (0, 10]  (10, 18]  (18, 25]  (25, 40]  (40, 90]
#sex
#female   0.612903  0.729730  0.759259  0.802198  0.770833
#male     0.575758  0.131579  0.120370  0.220930  0.176471

df.pivot_table("survived", "sex", ["new_age", "class"])
#new_age (0, 10]                   (10, 18]                   (18, 25]  \
#class     First Second     Third     First Second     Third     First
#sex
#female      0.0    1.0  0.500000  1.000000    1.0  0.523810  0.941176
#male        1.0    1.0  0.363636  0.666667    0.0  0.103448  0.333333
#new_age                      (25, 40]                      (40, 90]            \
#class      Second     Third     First    Second     Third     First    Second
#sex
#female   0.933333  0.500000  1.000000  0.906250  0.464286  0.961538  0.846154
#male     0.047619  0.115385  0.513514  0.071429  0.172043  0.280000  0.095238
#new_age
#class       Third
#sex
#female   0.111111
#male     0.064516

pd.set_option('display.width', 500)

#Apply&Lambda

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None) #gösterilecek olan maksimum kolon sayısı olmasın yani her kolonu göster diyoruz.
pd.set_option('display.width', 500)
df=sns.load_dataset("titanic")
df.head()

df["age2"]=df["age"]*2
df["age3"]=df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
df["age3"]/10

for col in df.columns:
   if "age" in col:
    print(col)
#>age
#age2
#age3

for col in df.columns:
   if "age" in col:
    print((df[col]/10).head())

#>0    2.2
#1    3.8
#2    2.6
#3    3.5
#4    3.5
#Name: age, dtype: float64
#0    4.4
#1    7.6
#2    5.2
#3    7.0
#4    7.0
#Name: age2, dtype: float64
#0    11.0
#1    19.0
#2    13.0
#3    17.5
#4    17.5
#Name: age3, dtype: float64


df[["age", "age2", "age3"]].apply(lambda x: x**2).head()
#>      age    age2     age3
#0   484.0  1936.0  12100.0
#1  1444.0  5776.0  36100.0
#2   676.0  2704.0  16900.0
#3  1225.0  4900.0  30625.0
#4  1225.0  4900.0  30625.0

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

#>   age  age2  age3
#0  2.2   4.4  11.0
#1  3.8   7.6  19.0
#2  2.6   5.2  13.0
#3  3.5   7.0  17.5
#4  3.5   7.0  17.5

#Öyle bir fonksiyon yazmak istiyorum ki uygulandığı değerleri standartlaştırsın
#istatistikçilerin yaygın kullandığı bir standartlaştırma-normalleştirme fonksiyonu yazalım.
#bütün gözlem birimlerinde ilgili değişnein ort.sını çıkarsın ve std. sapmasına bölsün diyelim:

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x- x.mean()) / s.std()).head()

#>        age      age2      age3
#0 -0.247166 -0.494331 -1.235828
#1  0.266484  0.532968  1.332420
#2 -0.118753 -0.237506 -0.593766
#3  0.170175  0.340350  0.850874
#4  0.170175  0.340350  0.850874


#apply'ın içine dışarıda tanımlanmış normal bi fonksiyon da yazabilir miyim? vet

def standart_scaler(col_name):
    return(col_name- col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

#        age      age2      age3
#0 -0.530005 -0.530005 -0.530005
#1  0.571430  0.571430  0.571430
#2 -0.254646 -0.254646 -0.254646
#3  0.364911  0.364911  0.364911
#4  0.364911  0.364911  0.364911

#KAydetme işlemi için:
df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()
df.head()

#Birleştirme İşlemleri
#1. hızlı seri pratik: concat 2. merge methodlarıyla

import numpy as np
import pandas as pd
m=np.random.randint(1, 30, size=(5,3))
#pd.DataFrame : sıfırdan dataframe oluşturmaya yarar.
df1= pd.DataFrame(m, columns=["var1", " var2", "var3"])
df1
#   var1   var2  var3
#0     2     10    11
#1    14      3    20
#2     3      4    12
#3    29     25    15
#4    25     17    20

df2=df1+99
df2
#   var1   var2  var3
#0     2     10    11
#1    14      3    20
#2     3      4    12
#3    29     25    15
#4    25     17    20

pd.concat([df1,df2])
#   var1   var2  var3
#0     2     10    11
#1    14      3    20
#2     3      4    12
#3    29     25    15
#4    25     17    20
#0   101    109   110
#1   113    102   119
#2   102    103   111
#3   128    124   114
#4   124    116   119

#index problemini gidermek için yani ardışık index numarası yazılması için:
#pd.concat([df1,df2], ignore_index=True)
#birleştirme işlemini satır bazında yaptı, concat'a argüman vererek sütun bazında da yapabiliriz.
#axis=0 ön tanımlı değeri yani satır demek, axis=1 yaparsak sütun bazında da birleştirme işlemi gerçekleşir.

#2.YOL : MERGE İLE BİRLEŞTİRME İŞLEMİ

df1= pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                   'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2= pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                   'start_date': [2010, 2009, 2014, 2019]})

#1. amacımız her çalışanın işe başlangıç tarihine erişmek istiyoruz:
#grup bilgisi, çalışan bilgisi, işe başlangıç tarihi bilgisi bir arada olsun istiyorum.

df3=pd.merge(df1, df2)
#>  employees        group  start_date
#0      john   accounting        2009
#1    dennis  engineering        2014
#2      mark  engineering        2010
#3     maria           hr        2019
#hangi değişkene göre birleştirmesi gerektiğni vermediğimiz halde alışanlara göre birleştirmiş
#özellikle belirtmek istersek on argümanı ile

pd.merge(df1, df2, on='employees')

df4=pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                  'manager': ['Caner', 'Mustafa', 'Berkcan']})
df4

#         group  manager
#0   accounting    Caner
#1  engineering  Mustafa
#2           hr  Berkcan

#Her çalışanın müdür bilgisine erişmek istiyoruz.
pd.merge(df3, df4)
#  employees        group  start_date  manager
#0      john   accounting        2009    Caner
#1    dennis  engineering        2014  Mustafa
#2      mark  engineering        2010  Mustafa
#3     maria           hr        2019  Berkcan








