dblogst = connect( 'mongodb://localhost/logsT' );

dblogst.createUser(
  {
    user: "logsuser",
    pwd: "logspassword", 
    roles: [ { role: "readWrite", db: "logsT" }]
  }
);

dbtlmanager = connect( 'mongodb://localhost/tlmanager' );

dbtlmanager.createUser(
  {
    user: "tluser",
    pwd: "tlpassword", 
    roles: [ { role: "readWrite", db: "tlmanager" }]
  }
);
