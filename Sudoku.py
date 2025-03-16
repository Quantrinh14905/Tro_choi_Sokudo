#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct edge {
    int u, v;
    int w;
};

const int maxn = 1001;
int n, m;
int parent[maxn], sz[maxn];
vector<edge> canh;

void make_set() {
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
        sz[i] = 1;
    }
}

int find(int v) {
    if (v == parent[v]) return v;
    return parent[v] = find(parent[v]);
}

bool Union(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return false; // Không thể gộp a, b vào với nhau
    if (sz[a] < sz[b]) swap(a, b);
    parent[b] = a;
    sz[a] += sz[b];
    return true;
}

void inp() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int x, y, w;
        cin >> x >> y >> w;
        edge e;
        e.u = x; e.v = y; e.w = w;
        canh.push_back(e);
    }
}

bool cmp(edge a, edge b) {
    return a.w < b.w;
}

void kruskal() {
    // Tạo cây khung cực tiêu rộng
    vector<edge> mst;
    int d = 0;
    
    // Sắp xếp danh sách cạnh theo chiều dài tăng dần
    sort(canh.begin(), canh.end(), cmp);

    // Bước 3 lặp
    for (int i = 0; i < m; i++) {
        if (mst.size() == n - 1) break;
        edge e = canh[i]; // Chọn cạnh e là cạnh nhỏ nhất
        if (Union(e.u, e.v)) {
            mst.push_back(e);
            d += e.w;
        }
    }

    // Trả về kết quả
    if (mst.size() != n - 1) {
        cout << "Đồ thị không liên thông!\n";
    } else {
        cout << "Tổng trọng số cây khung: " << d << "\n";
    }
}

int main() {
    inp();
    make_set();
    kruskal();
    return 0;
}
