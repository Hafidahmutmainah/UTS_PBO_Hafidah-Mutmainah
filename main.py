import json

# ==========================================
# 1. BAGIAN EMPLOYEE (KARYAWAN)
# ==========================================

class Employee:
    """Parent class untuk Employee"""
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        """Metode dasar perhitungan gaji"""
        return self.base_salary


class PermanentEmployee(Employee):
    """Child class untuk Karyawan Tetap (Inheritance)"""
    def __init__(self, emp_id, name, base_salary, bonus_code):
        super().__init__(emp_id, name, base_salary)
        self.bonus_code = bonus_code

    def calculate_salary(self):
        """OVERRIDE: Menghitung gaji karyawan tetap berdasarkan bonus_code"""
        bonus = 0
        if self.bonus_code == "PERF2026":
            bonus = 1500000
        elif self.bonus_code == "SENIOR10":
            bonus = 2500000
        elif self.bonus_code == "LEAD2026":
            bonus = 4000000
        return self.base_salary + bonus


class ContractEmployee(Employee):
    """Child class untuk Karyawan Kontrak (Inheritance)"""
    def __init__(self, emp_id, name, base_salary):
        super().__init__(emp_id, name, base_salary)

    def calculate_salary(self):
        """OVERRIDE: Menghitung gaji karyawan kontrak"""
        return self.base_salary


def process_employees(json_data):
    """POLIMORFISME: Memproses data employee dari file JSON"""
    print("=== LAPORAN DATA KARYAWAN ===")
    for data in json_data["employees"]:
        if data["is_permanent"]:
            emp = PermanentEmployee(
                data["emp_id"], 
                data["name"], 
                data["base_salary"], 
                data["bonus_code"]
            )
        else:
            emp = ContractEmployee(
                data["emp_id"], 
                data["name"], 
                data["base_salary"]
            )
        
        # Pemanggilan metode polimorfik calculate_salary()
        print(f"ID: {emp.emp_id} | Nama: {emp.name} | Gaji Total: Rp {emp.calculate_salary():,.2f}")


# ==========================================
# 2. BAGIAN SENSOR LOGS
# ==========================================

class SensorLog:
    """Parent class untuk Sensor Log"""
    def __init__(self, sensor_id, location, temperature, status, operator_id):
        self.sensor_id = sensor_id
        self.location = location
        self.temperature = temperature
        self.status = status
        self.operator_id = operator_id

    def get_details(self):
        """Metode dasar detail sensor"""
        return f"Sensor {self.sensor_id}"


class CriticalSensorLog(SensorLog):
    """Child class untuk Sensor berstatus DANGER (Inheritance)"""
    def __init__(self, sensor_id, location, temperature, status, operator_id):
        super().__init__(sensor_id, location, temperature, status, operator_id)

    def get_details(self):
        """OVERRIDE: Format khusus untuk status bahaya/DANGER"""
        op = self.operator_id if self.operator_id is not None else "Tidak Diketahui"
        return f"[BAHAYA!] Sensor {self.sensor_id} di {self.location} | Suhu: {self.temperature}°C | Operator: {op}"


class NormalSensorLog(SensorLog):
    """Child class untuk Sensor berstatus NORMAL / WARNING (Inheritance)"""
    def __init__(self, sensor_id, location, temperature, status, operator_id):
        super().__init__(sensor_id, location, temperature, status, operator_id)

    def get_details(self):
        """OVERRIDE: Format khusus untuk status normal atau warning"""
        return f"[INFO] Sensor {self.sensor_id} di {self.location} | Suhu: {self.temperature}°C | Status: {self.status}"


def process_sensor_logs(json_data):
    """POLIMORFISME: Memproses data sensor_logs dari file JSON"""
    print("\n=== LAPORAN MONITORING SENSOR ===")
    for data in json_data["readings"]:
        if data["status"] == "DANGER":
            sensor = CriticalSensorLog(
                data["sensor_id"], 
                data["location"], 
                data["temperature"], 
                data["status"], 
                data["operator_id"]
            )
        else:
            sensor = NormalSensorLog(
                data["sensor_id"], 
                data["location"], 
                data["temperature"], 
                data["status"], 
                data["operator_id"]
            )
        
        # Pemanggilan metode polimorfik get_details()
        print(sensor.get_details())


# ==========================================
# EKSEKUSI UTAMA PROGRAM
# ==========================================
if __name__ == "__main__":
    # Membaca file employee.json
    try:
        with open('employee.json', 'r') as file:
            emp_json = json.load(file)
            process_employees(emp_json)
    except FileNotFoundError:
        print("File employee.json belum dibuat di folder ini!")

    print("-" * 60)

    # Membaca file sensor_logs.json
    try:
        with open('sensor_logs.json', 'r') as file:
            sensor_json = json.load(file)
            process_sensor_logs(sensor_json)
    except FileNotFoundError:
        print("File sensor_logs.json belum dibuat di folder ini!")