# Email Error / 邮件中包含的错误
- ```Type Error``` : 座位类型错误。 座位被禁用或座位被预约
- ```Status Error``` : 座位状态不可用。 座位不在可预约状态
- ```{"success":false,"message":"已经存在预约记录，不能重复预约！"}``` : 同message

# Log Error / 日志中包含的错误
- ```Type:2``` / ```Type:3``` : 座位被禁用或占用
- ```Type:(非1/2/3)``` : 当前选中的seat_id是墙或者空的
- ```Status is (非1)``` : 座位二次验证时失效  (这种情况一般不出现)
- ```Email Error``` : 邮箱错误，我还没遇到过，反正检查就行了
- ```Failed 3 times. Check your username and password. Exiting.``` : 登录失败多次，请检查学号及密码