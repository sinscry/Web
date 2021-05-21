package po;

//user持久类
public class MyUser {
    private Integer uid;
    private String uname;
    private String usex;

    public MyUser(){}

    public void setUname(String uname) {
        this.uname = uname;
    }

    public void setUid(Integer uid) {
        this.uid = uid;
    }

    public void setUsex(String usex) {
        this.usex = usex;
    }

    public String getUname() {
        return uname;
    }

    public Integer getUid() {
        return uid;
    }

    public String getUsex() {
        return usex;
    }

    @Override
    public String toString(){
        return "User[uid=" + uid + ",uname=" + uname + ",usex=" + usex + "]";
    }
}
