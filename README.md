# 比奇堡财经视频 Skill

把财经、商业、职场和消费选题制作成“角色困境 → 机制解释 → 现实映射”的横版口播动画工作流。

默认角色世界是比奇堡，但它不是绑定项。只要替换角色资产和角色功能表，就可以迁移为《瑞克和莫蒂》《猫和老鼠》《名侦探柯南》、原创角色，或其他已获得授权的角色体系。

## 包含什么

- 高留存口播稿：2 秒钩子、具体困境、机制递进、现实映射与可执行收束。
- 元素化静态合成分镜：角色动作、道具、场景元素、台词内入场顺序与最终槽位。
- 原子素材流程：角色与可独立运动道具分开生成、抠图、裁切与质量审查。
- Remotion 剪辑规则：固定背景、台词驱动的元素入场、克制动效、构图和字幕安全区验收。
- 一个无依赖的素材清单校验脚本。

## 安装

将整个仓库作为一个 Codex Skill 文件夹安装到本机 skills 目录：

```bash
git clone https://github.com/<your-account>/bikini-bottom-econ-video-skill.git
cp -R bikini-bottom-econ-video-skill ~/.codex/skills/
```

重新打开 Codex 后，可以直接使用 `$bikini-bottom-econ-video-skill`，也可让系统按任务自动匹配。

## 典型使用方式

```text
用 $bikini-bottom-econ-video-skill 写一篇“幸存者偏差”的 5 分钟比奇堡财经口播稿，
再输出可用于 Remotion 的横版元素化分镜和资产清单。
```

```text
用 $bikini-bottom-econ-video-skill 将角色体系改成名侦探柯南：
柯南负责调查机制，小五郎代表直觉误判，灰原代表数据与专业视角。
```

## 角色体系替换

角色不只是外观，首先是叙事功能。替换时先建立功能表，而不是逐个替换名字：

| 默认功能 | 比奇堡示例 | 可替换角色类型 |
| --- | --- | --- |
| 经营者 / 规则制定者 | 蟹老板 | 平台、企业主、反派、组织负责人 |
| 普通行动者 | 海绵宝宝 | 员工、消费者、侦探助手、主角 |
| 直觉误区 | 派大星 | 冲动型角色、普通旁观者 |
| 现实反问 / 观察者 | 章鱼哥 | 讽刺型角色、冷静旁观者 |
| 专业与实验 | 珊迪 | 科学家、侦探、工程师、数据角色 |

## 开源与内容权利

本仓库的工作流说明、模板和脚本采用 MIT License。仓库不包含，也不授予任何第三方角色、剧集画面、音乐、字体、商标或参考视频的使用权。发布、变现或商用前，请自行确认所用素材的授权。

## 发布到 GitHub

```bash
git init
git add .
git commit -m "初始化开源 Skill"
git branch -M main
git remote add origin https://github.com/<your-account>/bikini-bottom-econ-video-skill.git
git push -u origin main
```
