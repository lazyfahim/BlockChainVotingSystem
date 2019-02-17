using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Model;

namespace DAL
{
    public class ElectionRepository:Repository<Election>, IElectionRepository
    {
        public ElectionRepository(DbContext context)
            :base(context)
        {
            
        }
    }
}
