import javax.swing.JOptionPane;

public class Taller_18 {
    public static double sy, syx, r, sr,a0,a1,st,mediax,mediay,sumax,sumay,sumaxy,sumax2;

    public static void main(String[] args) throws Exception {
       
        double[] y={0.2,0.6,1.6,3.5,5.5,9.1,13.5};
        
        double[] x={1,2,3,4,5,6,7};

        valores(x, y);

        String mensaje=String.format("Desviavion estandar: %f\n Error estandar: %f\n Coeficiente de correlacion: %.2f " , sy,syx,r);
        
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
}
    