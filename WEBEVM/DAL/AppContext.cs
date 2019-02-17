using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNet.Identity.EntityFramework;
using Model;

namespace DAL
{
    public class AppContext:IdentityDbContext<User>
    {
        public AppContext()
            : base("name=DefaultConnection")
        {
            //Database.SetInitializer(new MigrateDatabaseToLatestVersion<AppContext, DAL.Migrations.Configuration>());
        }
        public DbSet<Election> Elections { get; set; }
        public DbSet<Nominee> Nominees { get; set; }
        public DbSet<Image> Images { get; set; }
    }
}
