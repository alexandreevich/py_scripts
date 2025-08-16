# Для быстрого открытия порта на тачке

# Библиотека для работы с подпроцессами
import subprocess

def open_port_and_restart():
    port = input("Введите номер порта для открытия: ").strip()

    if not port.isdigit():
        print("Ошибка: порт должен быть числом.")
        return

    try:
        # Открываем порт
        subprocess.run(["sudo", "ufw", "allow", port], check=True)
        print(f"Порт {port} открыт в UFW.")

        # Перезапускаем UFW
        subprocess.run(["sudo", "systemctl", "restart", "ufw"], check=True)
        print("UFW перезапущен.")

        # Проверяем статус
        subprocess.run(["sudo", "ufw", "status", "verbose"])
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {e}")

if __name__ == "__main__":
    open_port_and_restart()
