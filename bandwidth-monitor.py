import psutil
import time

def get_net_io():
    """
    Retrieves the current network I/O statistics.
    
    Returns:
    - Tuple of (bytes_sent, bytes_recv): The number of bytes sent and received.
    """
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def compute_bandwidth(interval=1):
    """
    Computes the network bandwidth based on the change in network I/O over a specified interval.
    
    
    Args:
    - interval (int): The time interval in seconds over which to measure the network I/O.
    
    Returns:
    - Tuple of (send_rate, recv_rate): The sending and receiving rates in Megabytes per second.
    """
    send1, recv1 = get_net_io()
    time.sleep(interval)
    send2, recv2 = get_net_io()
    
    # Convert bytes to megabytes
    send_rate = (send2 - send1) / interval / 1024 / 1024
    recv_rate = (recv2 - recv1) / interval / 1024 / 1024
    
    return send_rate, recv_rate

if __name__ == "__main__":
    try:
        print("Monitoring network bandwidth (press Ctrl+C to stop)...")
        while True:
            send_rate, recv_rate = compute_bandwidth()
            print(f"Send: {send_rate:.2f} MB/s, Receive: {recv_rate:.2f} MB/s")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
