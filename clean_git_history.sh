#!/bin/bash

# 显示警告信息并等待用户确认
echo "警告: 该操作将删除本地和远程仓库的所有提交历史！确定要继续吗? (y/n)"
read confirm

# 检查用户输入，如果不是 'y' 则退出脚本
if [ "$confirm" != "y" ]; then
    echo "操作已取消"
    exit 1
fi

# 获取当前分支名称并存储在变量中
current_branch=$(git rev-parse --abbrev-ref HEAD)

# 开始清理本地仓库
echo "正在清理本地仓库..."
# 创建一个新的无父节点的分支
git checkout --orphan temp_branch
# 将所有文件添加到暂存区
git add -A
# 创建一个新的提交
git commit -am "重置仓库历史记录"
# 删除原始分支
git branch -D $current_branch
# 将当前分支重命名为原始分支名
git branch -m $current_branch

# 清理远程仓库并建立分支追踪关系
echo "正在清理远程仓库..."
# 强制推送到远程仓库并设置上游分支
git push -f --set-upstream origin $current_branch

echo "仓库历史记录清理完成！"
