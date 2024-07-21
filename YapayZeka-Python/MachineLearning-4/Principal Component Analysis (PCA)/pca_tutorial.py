from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

iris = load_iris()
data = iris.data
feature_names = iris.feature_names
y = iris.target

df = pd.DataFrame(data, columns=feature_names)
df["sınıf"] = y

x = data

pca = PCA(n_components=2, whiten=True)
pca.fit(x)
x_pca = pca.transform(x)

print("Varyans oranı: ", pca.explained_variance_ratio_)
print("Toplam: ", sum(pca.explained_variance_ratio_))

df["p1"] = x_pca[:, 0]
df["p2"] = x_pca[:, 1]

colors = ["red", "green", "blue"]
for each in range(3):
    plt.scatter(df.p1[df.sınıf == each], df.p2[df.sınıf == each],
                color=colors[each], label=iris.target_names[each])

plt.legend()
plt.xlabel("P1")
plt.ylabel("P2")
plt.title("PCA ile 2D Görselleştirme")
plt.show()
