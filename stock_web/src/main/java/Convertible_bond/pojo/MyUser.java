package Convertible_bond.pojo;

public class MyUser {
    public String usr;
    public String stock_id;
    public String stock_nm;
    public double oprice;

    public void setOprice(double oprice) {
        this.oprice = oprice;
    }

    public void setStock_id(String stock_id) {
        this.stock_id = stock_id;
    }

    public void setStock_nm(String stock_nm) {
        this.stock_nm = stock_nm;
    }

    public void setUsr(String usr) {
        this.usr = usr;
    }

    public double getOprice() {
        return oprice;
    }

    public String getStock_id() {
        return stock_id;
    }

    public String getStock_nm() {
        return stock_nm;
    }

    public String getUsr() {
        return usr;
    }
    @Override
    public String toString(){ //为了方便查看结果，重写了toString方法
        return "User[usr=" + usr + ",stock_id=" + stock_id + ",stock_nm=" + stock_nm + ",oprice="+oprice+"]";
    }
}
