# 图书管理系统

一个基于 Flask 的图书管理系统，提供图书浏览、搜索和分类功能。

## 功能特性

- 图书列表展示（分页显示）
- 按分类筛选图书
- 按书名/作者搜索图书
- 图书详情页
- RESTful API 接口
- 响应式 Web 界面

## 技术栈

- **后端框架**: Flask 2.3.3
- **数据库**: SQLite + Flask-SQLAlchemy 3.1.1
- **前端**: Flask-Bootstrap 3.3.7.1
- **其他**: Werkzeug 2.3.7

## 图书分类

系统包含以下图书分类：

- 玄幻小说
- 都市小说
- 文学经典
- 动漫漫画

共计 130+ 本精选图书数据。

## 快速开始

### 安装依赖

```bash
cd book_management_system
pip install -r requirements.txt
```

### 初始化数据库

```bash
python init_db.py
```

### 启动应用

```bash
python app.py
```

应用将在 http://localhost:5000 启动

## API 接口

### 获取图书列表

```
GET /api/books?page=1&category=玄幻&search=
```

响应示例：
```json
{
  "books": [
    {
      "id": 1,
      "title": "斗破苍穹",
      "author": "天蚕土豆",
      "category": "玄幻",
      "publisher": "湖北少年儿童出版社",
      "publish_date": "2011-06",
      "isbn": "9787535363391",
      "price": 29.8,
      "stock": 50,
      "description": "萧炎，一个曾经拥有斗气修炼天赋的少年..."
    }
  ],
  "total": 130,
  "pages": 7,
  "current_page": 1
}
```

### 获取图书详情

```
GET /api/book/<book_id>
```

## 项目结构

```
book_management_system/
├── app.py              # 主应用文件
├── models.py           # 数据模型
├── database.py         # 数据库配置
├── init_db.py          # 数据库初始化脚本
├── requirements.txt    # 依赖列表
├── data/
│   └── books_data.py   # 图书数据
└── templates/
    ├── index.html      # 首页模板
    └── detail.html     # 详情页模板
```

## 数据模型

```python
class Book(db.Model):
    id              # 图书ID
    title           # 书名
    author          # 作者
    category        # 分类
    publisher       # 出版社
    publish_date    # 出版日期
    isbn            # ISBN
    price           # 价格
    stock           # 库存
    description     # 简介
```

## 作者

- **玄幻**: 天蚕土豆、辰东、忘语、耳根、唐家三少、我吃西红柿、蝴蝶蓝、鱼人二代、烽火戏诸侯、骁骑校、会说话的肘子、江南、郭敬明
- **文学**: 余华、钱钟书、老舍、鲁迅、曹雪芹、罗贯中、施耐庵、吴承恩、路遥、陈忠实、贾平凹、莫言、刘慈欣
- **动漫**: 井上雄彦、尾田荣一郎、岸本齐史、久保带人、谏山创、石田スイ、吾峠呼世晴、堀越耕平、ONE、芥见下下、荒川弘、富坚义博、鸟山明、青山刚昌、高桥留美子、空知英秋、真岛浩、川原砾、伏濑、丸山黄金、长月达平、晓枣、赤坂明、安达浩树、京都动画、Key、P.A.WORKS、Aniplex、新海诚、大今良时、绿川幸、漆原友纪、堀田由美、许斐刚、高桥阳一、安达充、和月伸宏、渡边信一郎、士郎正宗、押井守、Gainax、岩明均、大场鸫、5pb.

## 许可证

MIT
