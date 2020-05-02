# 认证链的实现
## 基础架构
- 报告获取模块
- 报告发送模块
- 报告验证服务
## 流程
1. 报告获取模块：获取enclave的认证报告，并存储到指定文件中
2. 读取文件中的报告并发送到区块链服务端
3. 区块链服务端访问验证服务进行验证
4. 发送数据