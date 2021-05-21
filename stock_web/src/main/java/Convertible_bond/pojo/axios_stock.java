package Convertible_bond.pojo;

public class axios_stock {
    private String name;
    private String stock_id;
    private double oprice;

    public void setStock_id(String stock_id) {
        this.stock_id = stock_id;
    }
    public void setName(String name){
        this.name=name;
    }
    public void setOprice(double oprice){
        this.oprice=oprice;
    }

    public String getStock_id() {
        return stock_id;
    }
    public String getName(){
        return name;
    }
    public double getOprice(){
        return oprice;
    }
}
