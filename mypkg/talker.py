import rclpy                     # ROS 2 のクライアントライブラリ
from rclpy.node import Node      # ノードを実装するための Node クラス
from std_msgs.msg import Int16   # 通信の型（16ビット符号付き整数）

rclpy.init()                     # rclpy の初期化（最初に1回）
node = Node("talker")            # ノード作成
pub = node.create_publisher(Int16, "countup", 10)  # 型、トピック名、キュー長
n = 0                            # カウント用変数


def cb():                        # タイマーで定期的に呼ばれるコールバック関数
    global n                     # 関数を抜けても n がリセットされないように
    msg = Int16()                # メッセージのオブジェクト
    msg.data = n                 # msg の持つ data に n を入れる
    pub.publish(msg)             # パブリッシュ
    n += 1


def main():
    node.create_timer(0.5, cb)   # 0.5 秒ごとに cb を呼ぶタイマー
    rclpy.spin(node)             # 実行（無限ループ）
