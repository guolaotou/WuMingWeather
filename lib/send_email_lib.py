import yaml, os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from logging import log
import logging


class Email():
    def __init__(self):
        # 获取文件全路径
        filename = os.path.join(os.path.dirname(__file__), '../config.yaml').replace("\\", "/")
        with open(filename) as f:
            config = yaml.load(f)
        self.config = config

    def send_email(self, text="这是一封测试邮件，请查收"):
        mail_host = 'smtp.163.com'
        # 163用户名
        mail_user = self.config.get("main").get("email").get("username")
        # 密码(部分邮箱为授权码)
        mail_pass = self.config.get("main").get("email").get("password")
        # 邮件发送方邮箱地址
        sender = self.config.get("main").get("email").get("username")
        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        receivers = self.config.get("main").get("email").get("email_to")

        print("receivers", receivers)
        # 设置email信息
        # 邮件内容设置
        message = MIMEText(text, 'plain', 'utf-8')
        # 邮件主题
        message['Subject'] = "今天的天气情况"
        # 发送方信息
        message['From'] = sender
        # 接受方信息
        message['To'] = receivers[0]

        logging.info("mail_pass: ", mail_pass)
        logging.info("sender: ", sender)

        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(mail_host, 25)
            # 登录到服务器
            smtpObj.login(mail_user, mail_pass)
            # 发送
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            # 退出
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误

if __name__ == "__main__":
    email = Email()
    email.send_email()
