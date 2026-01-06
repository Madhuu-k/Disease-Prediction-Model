// chartConfig.js (make sure you have this set up)
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Tooltip,
  Legend
} from "chart.js";
ChartJS.register(LineElement, PointElement, LinearScale, CategoryScale, Tooltip, Legend);
// ResultChart.jsx
import "../chartConfig";
import { Line } from "react-chartjs-2";
import { useMemo } from "react";

export default function ResultChart({ predictions }) {
  // Guard against empty or undefined predictions
  if (!predictions || predictions.length === 0) {
    return <p>No predictions available</p>;
  }
  const data = useMemo(() => ({
    labels: predictions.map((p) => p.disease),
    datasets: [
      {
        label: "Confidence (%)",
        data: predictions.map((p) => Math.round(p.confidence * 100)),
        borderColor: "rgba(76, 175, 80, 0.9)",   // line color
        backgroundColor: "rgba(76, 175, 80, 0.3)", // fill under line
        tension: 0.3, // smooth curves
        fill: true,   // area under line filled
        pointRadius: 5, // size of points
        pointBackgroundColor: "rgba(76, 175, 80, 0.9)"
      }
    ]
  }), [predictions]);

  const options = useMemo(() => ({
    responsive: true,
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: (ctx) => `${ctx.raw}%`
        }
      }
    },
    scales: {
      y: {
        min: 0,
        max: 100,
        ticks: {
          callback: (value) => `${value}%`
        }
      }
    }
  }), []);

  return <Line data={data} options={options} />;
}