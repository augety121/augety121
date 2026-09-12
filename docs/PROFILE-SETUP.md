# 浅色动态主页维护说明

## 页面入口

- 默认中文：根目录 `README.md`。
- 英文：根目录 `README.en.md`，由顶部语言链接切换。
- GitHub README 不执行页面 JavaScript；这里使用真正的文档链接，不伪装即时切换按钮。
- 新版资源统一位于 `assets/profile/`。仓库原来的图片与旧脚本保留，但新版 README 不再引用它们。

## 视觉系统

浅蓝 `#438BC5`、薄荷绿 `#309F8B`、深灰蓝文字 `#243B53`，搭配近白色背景。

头图、关注方向卡片、项目卡片、开发方式流程图与页脚采用 SVG 内嵌 CSS 循环动画，缓慢流动的路径代表知识、上下文与行动。无 JavaScript、外部字体、远程图片嵌套，不需要生成图片服务。头图只保留文字节点，不使用编号。

头图、关注方向卡片、项目卡片、开发方式流程图、贡献动画和统计卡片有单独的窄屏版本。`picture` 在 600px 以下切换布局。减少动态效果偏好下，使用静态 SVG 与真实贡献日历。即使阅读器不支持动画，主体文字也始终可见。

重新生成设计资源：

```bash
python scripts/build_profile_assets.py
python scripts/frame_contribution_snake.py
python -m unittest discover -s tests -v
```

不要运行旧的 `generate_profile_visuals.py` 来修改新版资源；它只负责旧版目录。

`frame_contribution_snake.py` 读取已有的真实 `contribution-snake.svg`，只嵌入浅色外框和中英文标题，不修改贡献格子、运动轨迹或动画关键帧。生成的 `contribution-zh.svg`、`contribution-en.svg` 及 `contribution-mobile-*.svg` 供 README 使用。数据更新工作流先运行 `snk`，再生成外框；不需要额外令牌或图片服务。

## 动态组件与来源

| 组件 | 用途 | 依赖与失败行为 |
| --- | --- | --- |
| [Platane/snk](https://github.com/Platane/snk) | 把真实贡献日历变成贪吃蛇 SVG | Actions 生成并提交到本仓库；访客不访问生成接口 |
| [Skill Icons](https://github.com/tandpfun/skill-icons) | 浅色技术栈图标 | `skillicons.dev` 外链；加载失败时仍保留下方技术栈文字 |
| 自有统计卡片 | 中文和英文公开活动概览 | GitHub GraphQL API + 仓库内 Python 脚本，无共享统计卡片服务 |

动画播放和数据更新是两回事：SVG 在浏览器中循环播放，数据每天更新一次，并非实时在线状态。GitHub 的图片缓存和 Actions 排队可能延迟显示。

## 自动更新

工作流：`.github/workflows/update-profile-stats.yml`，显示名称 **Update Profile Statistics**。

- 每天北京时间 08:15 计划运行；GitHub 调度可能延迟。
- 支持 `workflow_dispatch` 手动运行。
- 修改对应生成脚本或工作流时，在当前分支触发一次更新，便于合并前验收。
- 定时运行和手动运行入口需要该工作流位于默认分支；设计分支首次推送通过 `push` 触发。
- `generate` 任务只读权限，读取数据并运行第三方动画生成器；`publish` 任务才有写入权限，仅提交十个指定 SVG 文件。
- 使用 GitHub 自动提供的 `GITHUB_TOKEN`，无需创建个人访问令牌，也不读取私人项目内容。
- API 或生成过程失败时，任务报错，不提交部分结果，线上保留上次成功的图片。
- 仓库分支保护若禁止 bot 直接推送，发布步骤会失败，需要仓库所有者决定如何允许这些生成资源更新；不要为此关闭全部保护。

首次启用：将改动合并至 `main` 后，进入 **Actions → Update Profile Statistics → Run workflow → main → Run workflow**。首次推送若已运行成功，可直接查看生成资源。

若使用下载包上传，必须保留 `.github/workflows/` 目录结构；把 YAML 放在仓库根目录不会成为 GitHub Actions 工作流。

## 统计口径

- 公开原创仓库：当前用户拥有的公开、非 fork 仓库。
- 获得星标：上述仓库的星标总数；支持分页，不限前 100 个。
- 近一年贡献：GitHub contribution calendar 返回的近一年贡献总数。
- 关注者：GitHub 公开关注者数量。
- 中英文卡片来自同一次采集，使用同一个更新时间。

未更新的初始卡片显示破折号与“等待首次更新”，不使用演示数字。`--placeholder` 仅用于初始搭建，生产工作流不调用此选项。

## 验证

`Check Profile` 工作流检查双语图片链接、SVG 安全性、动静态版本、统计本地化、分页与失败处理，以及设计资源是否可重复生成。网络数据更新与社区动画生成还应以 `Update Profile Statistics` 的实际运行结果为准。

这个 README 介绍开发方向与公开实践，不把实验项目表述为已达到生产级，也不自动把项目路线图写成已实现能力。
