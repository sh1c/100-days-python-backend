阶段 0｜前置准备（第 1 周，Day1-7）
D1  
- [X] 装 Python 3.11、VS Code、Git、Postman（1）  
- [X] 注册 GitHub，建 100-days-python-backend 私有仓库（0.5）  
- [X] 把本打卡模板 README.md 推到仓库（0.5）

D2  
- [X] 命令行 10 个常用指令各敲 5 遍（1）  
- [ ] 配 oh-my-zsh + 插件（git／z）（1）

D3  
- [X] Git 三板斧练习：新建 repo→add→commit→push（1）  
- [ ] 开分支 feature/test → 提 PR → 自己合并（1）

D4  
- [ ] 装 Docker Desktop，跑 hello-world 容器（1）  
- [ ] 给 Docker 配阿里云镜像加速（0.5）

D5  
- [x] 浏览器收藏 3 个官方文档（0.5）  
- [x] 加入 V2EX-Python、知乎专栏，发「Day5 报道帖」记录（0.5）

D6  
- [ ] 通读 PEP8，用 black 格式化一段烂代码（1）  
- [ ] 装 pre-commit，配 black+isort，提交一次（1）

D7  
- [ ] 周复盘：写 Week0 日报（要点、踩坑、耗时）→ 推仓库（1）

---

阶段 1｜Python 硬核基础（第 2-5 周，Day8-35）
「每日模板」  
上午 1h：读《流畅的Python》对应章节  
下午 1h：手敲代码 + pytest  
晚上 1h：commit & 写「今日卡片」笔记（markdown 放 docs/daily/）

Day8-9  列表推导式 + 生成器表达式（yield）  
Day10-11 装饰器（logger、timer、retry）  
Day12-13 with 上下文管理（写两个自定义类）  
Day14 周复盘 + 刷 3 道 LeetCode 数组简单题

Day15-16 *args/**kwargs + 函数注解  
Day17-18 threading 写生产者消费者队列  
Day19-20 multiprocessing 对比多线程耗时实验  
Day21 周复盘 + 博客输出《GIL 不是洪水猛兽》

Day22-23 asyncio 事件循环，写 echo server  
Day24-25 aiohttp 并发下载 10 张图片  
Day26-27 pytest 参数化 + fixture，给 echo server 写测试  
Day28 周复盘 + 覆盖率提升到 90%

Day29-30 argparse 文档通读，记账本 CLI 骨架  
Day31-32 JSON 存取、datetime 处理、异常自定义  
Day33-34 补测试到 100%，补黑色/排序钩子  
Day35 阶段 1 收官：  
- [ ] 把记账本项目重命名为 account-cli，打 tag v1.0  
- [ ] 运行录屏 → 放 README → 推 GitHub  
- [ ] 写阶段总结：代码量 1.1k 行，测试 52 条，覆盖率 100%

---

阶段 2｜关系型数据库 & Web 基础（第 6-9 周，Day36-63）
「每日节奏」  
上午 1.5h：LeetCode-SQL 1 题 + explain 分析  
下午 1.5h：Flask/Django 代码  
晚上 1h：Alembic 迁移 or 博客接口

Day36-37 装 PostgreSQL，手打 CRUD 10 条命令  
Day38-39 事务/索引/left join 实验  
Day40-41 LeetCode-SQL 中等题 5 道  
Day42 周复盘 + 画「SQL 执行计划」思维导图

Day43-44 原生 psycopg3 写 DAO 层  
Day45-46 同需求改 SQLAlchemy ORM，对比耗时  
Day47-48 Alembic 初始化，新增字段、回滚一次  
Day49 周复盘 + 博客《ORM 真的慢吗？》

Day50-51 Flask 最小博客：Blueprint、404、日志  
Day52-53 JWT 登录（access+refresh）  
Day54-55 分页、标签、N+1 检测（SQLAlchemy selectinload）  
Day56 周复盘 + 压测 200 并发 QPS 记录

Day57-58 用 Django 复刻同一套接口  
Day59-60 DRF viewset + pagination + JWT  
Day61-62 单元测试 80 条，覆盖率 87%  
Day63 阶段 2 收官：  
- [ ] 仓库开新目录 blog-backend-flask / blog-backend-django  
- [ ] README 放 API 文档 + 压测截图  
- [ ] 写技术对比文章《Flask vs Django 同一接口开发差异》

---

阶段 3｜进阶框架 & 工程化（第 10-14 周，Day64-98）
「每日节奏」  
上午 2h：FastAPI 官方教程 + 异步代码  
下午 2h：Docker/CICD 实战  
晚上 1h：Celery/Redis 踩坑笔记

Day64-65 FastAPI 依赖注入、SQLModel、OpenAPI  
Day66-67 WebSocket 聊天室 Demo  
Day68-69 布隆过滤器 + Redis 缓存穿透实战  
Day70 周复盘 + 镜像体积 280 MB → 60 MB 记录

Day71-72 RabbitMQ 装起来，发邮件任务队列  
Day73-74 Celery beat 每日热门统计  
Day75-76 docker-compose 编排（app/pg/redis/nginx）  
Day77 周复盘 + 画架构图（draw.io）

Day78-79 GitHub Actions 写 lint+test 流程  
Day80-81 自动构建镜像 → 推阿里云 ACR  
Day82-83 Webhook 到云服务器自动部署  
Day84 周复盘 + 域名 + Let’s Encrypt HTTPS

Day85-90 社区论坛 SaaS 多租户开发（按天细分接口）  
Day91-92 实时通知 WebSocket + Redis 发布订阅  
Day93-94 后台管理 FastAPI-Admin 集成  
Day95-96 单元测试补到 85%，压测 1k 并发  
Day97-98 阶段 3 收官：  
- [ ] 仓库打 tag v3.0，放线上地址（https://bbs-demo.xxx.com）  
- [ ] README 含架构图、性能报告、CI badge  
- [ ] 写《从 0 到 1 容器化部署 FastAPI  SaaS》博客

---

阶段 4｜面试冲刺（第 15-16 周，Day99-112）
「每日节奏」  
上午 1h：刷 LeetCode 高频 2 题  
下午 2h：背八股 + 录音自问自答  
晚上 1h：改简历 + 模拟面试

Day99-100 Python 八股 15 问（GIL/垃圾回收/元类）  
Day101-102 Web 八股 15 问（JWT/CORS/REST）  
Day103-104 DB 八股 15 问（ACID/隔离/索引）  
Day105-106 系统 15 问（进程线程协程/epoll）  
Day107 简历 0.9 版，STAR 量化数字  
Day108 GitHub 精选 3 项目，README 统一风格  
Day109-110 同伴模拟面试 3 轮，录屏回看  
Day111 90 秒电梯陈述背熟，常见陷阱写便签  
Day112 总复盘：  
- [ ] 112 天打卡全部勾完  
- [ ] 把「100-days-python-backend」仓库设为公开  
- [ ] 发总结帖：Day1→Day112 时间轴 + 收获 + 面经