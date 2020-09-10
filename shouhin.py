import mysql.connector

from dataclasses import dataclass

@dataclass
class Shouhin:
    sid: int
    sname: str
    tanka: int

class ShouhinDB:
    def __init__(self) -> None:
        self.con = mysql.connector.connect(
            user = 'root',
            password = '',
            database = 'han2',
        )

        self.cur = self.con.cursor(prepared=True)
    
    def close(self):
        self.con.close()

    def get_all(self) -> list:
        self.cur.execute('SELECT * FROM shouhin')
        rows = self.cur.fetchall()

        ret = []
        for row in rows:
            sid,sname,tanka,cid = row
            s = Shouhin(sid,sname,tanka)
            ret.append(s)
        
        return ret

    def get(self,sid) -> Shouhin:
        self.cur.execute('SELECT * FROM shouhin WHERE sid=?',[sid])
        row = self.cur.fetchone()
        sid,sname,tanka,cid = row
        return Shouhin(sid,sname,tanka)
    
    def insert(self,shouhin):
        self.cur.execute('INSERT INTO shouhin (sname,tanka) VALUES(?,?)',[shouhin.sname,shouhin.tanka])
        self.con.commit()

    def update(self,shouhin):
        self.cur.execute('UPDATE shouhin SET sname=?,tanka=? WHERE sid=?',[shouhin.sname,shouhin.tanka,shouhin.sid])
        self.con.commit()

    def delete(self,sid):
        self.cur.execute('DELETE FROM shouhin WHERE sid=?',[sid])
        self.con.commit()

if __name__ == "__main__":
    db = ShouhinDB()

    # all = db.get_all()
    # for s in all:
    #     print(s)

    # s = db.get(2)
    # print(s)

    # s = Shouhin(0,'かき',90)
    # db.insert(s)

    # s = Shouhin(8,'かき1',120)
    # db.update(s)    

    # db.delete(8)
    db.close()