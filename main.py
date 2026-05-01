def simple_ai_reply(message):
    # 简单规则AI
    if "退款" in message:
        return "您可以在订单页面申请退款，我可以帮您查看流程。"
    elif "订单" in message:
        return "请提供订单号，我帮您查询订单状态。"
    elif "你好" in message or "您好" in message:
        return "您好！我是AI客服，请问有什么可以帮您？"
    elif "发货" in message:
        return "一般下单后1-3天内发货，请耐心等待。"
    else:
        return "抱歉，我还在学习中，可以换个说法试试～"


def main():
    print("=== AI客服系统已启动（输入 exit 退出）===")

    while True:
        user_input = input("你：")

        if user_input.lower() == "exit":
            print("AI：感谢使用，再见！")
            break

        reply = simple_ai_reply(user_input)
        print("AI：", reply)


if __name__ == "__main__":
    main()
