# 100-days-python-backend 打卡仓库

&gt; 16 周后端进阶计划 | 112 天可量化打卡 | 目标：能写、能测、能部署、能面试

---

## 1️⃣ 阶段总览
| 阶段 | 周 | 起止日期 | 关键词 | 输出物 |
|---|---|---|---|---|
| 0 | 1 | Day01-07 | 环境+Git+Docker | 绿色方阵第一排 |
| 1 | 4 | Day08-35 | Python 硬核 | account-cli v1.0 |
| 2 | 4 | Day36-63 | SQL+Web | 博客双框架 |
| 3 | 5 | Day64-98 | 工程化+容器 | 论坛 SaaS+HTTPS |
| 4 | 2 | Day99-112 | 面试 | 简历+电梯陈述 |

---

## 2️⃣ 今日打卡（每天只改这里）
| 项目 | 勾选 | 耗时 | 备注 |
|---|---|---|---|
| 阅读/视频 | ✅ | 5 min |  |
| 编码 | ✅ | 5 min |  |
| 单元测试 | ⬜ | 0 min |  |
| 复盘 & 笔记 | ⬜ | 0 min |  |
| 提交 & Push | ⬜ | 0 min |  |

**今日总结：**  
&lt;!-- day1环境配置完成 --&gt;

**明日计划：**  
&lt;!-- day2 D2 D3 完成 --&gt;

---

## 3️⃣ 可视化进度
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=SH1C&theme=radical&hide=prs,issues)

&gt; 绿色格子每天 1 commit 打底，断一天就补双倍。

---

## 4️⃣ 项目清单（链接指向本仓库子目录）
1. [account-cli](./account-cli) — CLI 记账本 | 阶段 1  
2. [blog-backend-flask](./blog-backend-flask) — Flask 版博客 | 阶段 2  
3. [blog-backend-django](./blog-backend-django) — Django 版博客 | 阶段 2  
4. [community-saas](./community-saas) — 多租户论坛 | 阶段 3  

&gt; 每个子目录 README 再放运行录屏 + 压测报告 + 线上地址。

---

## 5️⃣ 每日 checklist 仓库地址
长期有效的模板 & 112 天详细任务列表：  
https://github.com/SH1C/100-days-python-backend/blob/main/docs/roadmap.md

---

## 6️⃣ 如何快速开始（写给未来的自己）
```bash
# 克隆
git clone https://github.com/{{user}}/100-days-python-backend.git
cd 100-days-python-backend

# 创建今日分支
git checkout -b day$(date +%j)

# 编辑 README.md → 把 ⬜ 改成 ✅，写总结
code README.md

# 提交
git add .
git commit -m "Day$(date +%j) ✅ xxxx"
git push origin day$(date +%j):main
