function fillExample() {
    const samples = [
    [25, 50, 15, 18, 22, 12, 0.5, 5, 20],
    [90, 180, 60, 58, 70, 25, 1.0, 15, 30],
    [120, 200, 80, 75, 90, 30, 1.5, 20, 35],
    [60, 110, 35, 40, 45, 18, 0.7, 10, 25],
    [10, 30, 5, 8, 12, 5, 0.3, 2, 10],
    [160, 250, 100, 95, 110, 35, 2.0, 30, 50],
    [45, 90, 25, 28, 33, 15, 0.6, 8, 18],
    [75, 130, 50, 52, 60, 22, 0.9, 12, 28],
    [30, 60, 20, 22, 26, 10, 0.4, 6, 15],
    [200, 280, 120, 110, 130, 40, 2.5, 40, 55]
];
    const sample = samples[Math.floor(Math.random() * samples.length)];
    const fields = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3'];

    fields.forEach((field, idx) => {
        document.getElementsByName(field)[0].value = sample[idx];
    });
}
