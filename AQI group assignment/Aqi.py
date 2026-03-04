import csv
from datetime import datetime
from collections import defaultdict

BREAKPOINTS = {
    "pm25": [
        (0.0, 12.0, 0, 50),
        (12.1, 35.4, 51, 100),
        (35.5, 55.4, 101, 150),
        (55.5, 150.4, 151, 200),
        (150.5, 250.4, 201, 300),
        (250.5, 350.4, 301, 400),
        (350.5, 500.4, 401, 500),
    ],
    "pm10": [
        (0, 54, 0, 50),
        (55, 154, 51, 100),
        (155, 254, 101, 150),
        (255, 354, 151, 200),
        (355, 424, 201, 300),
        (425, 504, 301, 400),
        (505, 604, 401, 500),
    ],
    "no2": [
        (0, 53, 0, 50),
        (54, 100, 51, 100),
        (101, 360, 101, 150),
        (361, 649, 151, 200),
        (650, 1249, 201, 300),
        (1250, 1649, 301, 400),
        (1650, 2049, 401, 500),
    ],
    "so2": [
        (0, 35, 0, 50),
        (36, 75, 51, 100),
        (76, 185, 101, 150),
        (186, 304, 151, 200),
        (305, 604, 201, 300),
        (605, 804, 301, 400),
        (805, 1004, 401, 500),
    ],
    "o3": [
        (0, 54, 0, 50),
        (55, 70, 51, 100),
        (71, 85, 101, 150),
        (86, 105, 151, 200),
        (106, 200, 201, 300),
    ],
    "co": [
        (0.0, 4.4, 0, 50),
        (4.5, 9.4, 51, 100),
        (9.5, 12.4, 101, 150),
        (12.5, 15.4, 151, 200),
        (15.5, 30.4, 201, 300),
        (30.5, 40.4, 301, 400),
        (40.5, 50.4, 401, 500),
    ],
}

def calculate_aqi(concentration, pollutant):
    if concentration is None:
        return None

    for bp_lo, bp_hi, aqi_lo, aqi_hi in BREAKPOINTS[pollutant]:
        if bp_lo <= concentration <= bp_hi:
            aqi = ((aqi_hi - aqi_lo) / (bp_hi - bp_lo)) * \
                  (concentration - bp_lo) + aqi_lo
            return round(aqi)

    return 500

def calculate_monthly_aqi(csv_file):

    monthly_data = defaultdict(list)

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                timestamp = datetime.fromisoformat(row["event_timestamp"])
            except:
                continue

            year = timestamp.year
            month = timestamp.month

            pollutants = ["pm25", "pm10", "no2", "so2", "o3", "co"]
            aqi_values = []

            for pollutant in pollutants:
                try:
                    value = float(row[pollutant])
                    aqi = calculate_aqi(value, pollutant)
                    if aqi is not None:
                        aqi_values.append(aqi)
                except:
                    continue

            if len(aqi_values) == 0:
                continue

            final_aqi = max(aqi_values)
            monthly_data[(year, month)].append(final_aqi)


    print("\n MONTHLY AQI REPORT \n")

    for (year, month) in sorted(monthly_data):
        avg_aqi = sum(monthly_data[(year, month)]) / len(monthly_data[(year, month)])
        print(f"{year} - {month:02d} : Average AQI = {round(avg_aqi)}")

    print("\n")


if __name__ == "__main__":
    calculate_monthly_aqi("delhi_air_quality_feature_store_processed.csv")