import javax.swing.JOptionPane;

public class Taller_19 {
    public static double sy, syx, r, sr,a0,a1,st,mediax,mediay,sumax,sumay,sumaxy,sumax2;

    public static void main(String[] args) throws Exception {
       
        double[] y={0.2,0.6,1.6,3.5,5.5,9.1,13.5};
        
        double[] x={1,2,3,4,5,6,7};
        double m=pendiente(x, y);

        double b=b(x,y,m);

        valores(x, y);

        String mensaje=String.format("Formula: y= %.3fx+(%.3f) \nDesviavion estandar: %f \nError estandar: %f \nCoeficiente de correlacion: %.2f ",m,b, sy,syx,r);
        
        JOptionPane.showMessageDialog(null , mensaje);
        
        


    }
    public static void valores(double[] x,double[] y){
        double n=x.length;
        for (int i = 0; i < x.length; i++) {
            sumax+=x[i];
            sumay+=y[i];
            sumaxy+=y[i]*x[i];
            sumax2+=x[i]*x[i];


        }
        mediax=sumax/n;
        mediay=sumay/n;
        a1=(n*sumaxy-sumax*sumay)/(n*sumax2-sumax*sumax);
        a0=(mediay-mediax*a1);

        for (int i = 0; i < y.length; i++) {
            st+=(y[i]-mediay)*(y[i]-mediay);
            sr+=(y[i]-a0-a1*x[i])*(y[i]-a0-a1*x[i]);
        }
        sy=Math.sqrt(st/(n-1));
        syx=Math.sqrt(sr/(n-2));

        r=Math.sqrt((st-sr)/st)*100;

    }
    
    public static double pendiente(double[] x,double[] y){
        double pendient=0;
        if (x.length==y.length){
            double sumaX=0;
            double sumaY=0;
            double sumaXY=0;
            double sumaX2=0;
            int n=y.length;


            for (int i = 0; i < n; i++) {

                double xi=x[i];
                double yi=y[i];
                sumaX+=xi;
                sumaY+=yi;
                sumaXY+=xi*yi;
                sumaX2+=xi*xi;
            }

            pendient= (n*sumaXY-(sumaX*sumaY))/(n*sumaX2-(sumaX*sumaX));
        }  

        return pendient;
    }

    public static double b(double[] x,double[] y, double m) {
        
        double sumaX=0;
        double sumaY=0;
        for (int i = 0; i < x.length; i++) {
            sumaX+=x[i];
            sumaY+=y[i];
        }

        int n=x.length;

        double b=(sumaY/n)-m*(sumaX/n);
        return b;
    }
}
    