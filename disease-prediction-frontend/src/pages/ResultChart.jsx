import "../chartConfig";
import { Bar } from "react-chartjs-2";

export default function ResultChart({ predictions }) {
  const data = {
    labels: predictions.map((p) => p.disease),
    datasets: [
      {
        label: "Confidence (%)",
        data: predictions.map((p) =>
          Math.round(p.confidence * 100)
        ),
        backgroundColor: "rgba(76, 175, 80, 0.7)",
        borderRadius: 6
      }
    ]
  };

  const options = {
    responsive: true,
    indexAxis: "y", // horizontal bars
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: (ctx) => `${ctx.raw}%`
        }
      }
    },
    scales: {
      x: {
        min: 0,
        max: 100,
        ticks: {
          callback: (value) => `${value}%`
        }
      }
    }
  };

  return <Bar data={data} options={options} />;
}
