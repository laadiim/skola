sing System;
using System.Drawing;
using System.Windows.Forms;

namespace MandelbrotSet
{
    public partial class MainForm : Form
    {
        private const int MaxIterations = 1000;
        private const double ZoomFactor = 0.1;
        private const int InitialWidth = 800;
        private const int InitialHeight = 600;

        private Bitmap mandelbrotImage;
        private double zoom = 1.0;
        private double offsetX = -0.5;
        private double offsetY = 0;

        public MainForm()
        {
            InitializeComponent();
            mandelbrotImage = new Bitmap(InitialWidth, InitialHeight);
            DrawMandelbrotSet();
        }

        private void MainForm_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawImage(mandelbrotImage, 0, 0);
        }

        private void DrawMandelbrotSet()
        {
            for (int x = 0; x < mandelbrotImage.Width; x++)
            {
                for (int y = 0; y < mandelbrotImage.Height; y++)
                {
                    double a = 3.5 * (x - mandelbrotImage.Width / 2.0) / (0.5 * zoom * mandelbrotImage.Width) + offsetX;
                    double b = 2.0 * (y - mandelbrotImage.Height / 2.0) / (0.5 * zoom * mandelbrotImage.Height) + offsetY;

                    double ca = a;
                    double cb = b;

                    int n = 0;
                    while (n < MaxIterations)
                    {
                        double aa = a * a - b * b;
                        double bb = 2 * a * b;
                        a = aa + ca;
                        b = bb + cb;

                        if (Math.Abs(a + b) > 16)
                        {
                            break;
                        }

                        n++;
                    }

                    int brightness = 255 - (int)(255.0 * n / MaxIterations);
                    mandelbrotImage.SetPixel(x, y, Color.FromArgb(brightness, brightness, brightness));
                }
            }

            Invalidate();
        }

        private void MainForm_MouseClick(object sender, MouseEventArgs e)
        {
            double zoomFactor = e.Button == MouseButtons.Left ? (1 / ZoomFactor) : ZoomFactor;
            double newZoom = zoom * zoomFactor;

            double mouseRe = (e.X - mandelbrotImage.Width / 2.0) / (0.5 * zoom * mandelbrotImage.Width) + offsetX;
            double mouseIm = (e.Y - mandelbrotImage.Height / 2.0) / (0.5 * zoom * mandelbrotImage.Height) + offsetY;

            offsetX = mouseRe - (e.X - mandelbrotImage.Width / 2.0) / (0.5 * newZoom * mandelbrotImage.Width);
            offsetY = mouseIm - (e.Y - mandelbrotImage.Height / 2.0) / (0.5 * newZoom * mandelbrotImage.Height);
            zoom = newZoom;

            mandelbrotImage = new Bitmap(mandelbrotImage.Width, mandelbrotImage.Height);
            DrawMandelbrotSet();
        }
    }
}
