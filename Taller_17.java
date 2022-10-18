import javax.swing.JOptionPane;

public class Taller_17 {



    public static void main(String[] args) throws Exception {
       
        double[] y={4.5,6,9,12,17,24};
        double lny[]=new double[6];
        for (int i = 0; i < y.length; i++) {
            double x=Math.log(4.5);
            lny[i]=Math.log(y[i]);
        }

               
        double[] x={1,2,3,4,5,6};

        double m=pendiente(x, lny);

        double b=b(x,lny,m);

        String mensaje=String.format("ln(y)= %.3fX + %.3f", m,b);
        
        JOptionPane.showMessageDialog(null , mensaje);
        
        


    }


    public static double pendiente(double[] x,double[] y){

        double a1=0;

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

            a1= (n*sumaXY-(sumaX*sumaY))/(n*sumaX2-(sumaX*sumaX));
        }  

        return a1;
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

        double alfa= Math.exp(b);

        return Math.log(alfa);
    }

    


}
