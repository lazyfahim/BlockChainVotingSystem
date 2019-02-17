using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DAL
{
    public class UOW : IUOW
    {
        private AppContext context;

        public UOW(AppContext context)
        {
            this.context = context;
            this.context.Configuration.ProxyCreationEnabled = false;
            this.ElectionRepository = new ElectionRepository(context);
            this.UserRepository = new UserRepository(context);
        }
        public IUserRepository UserRepository { get; private set; }
        public IElectionRepository ElectionRepository { get; private set; }
        
        private bool disposed = false;

        public virtual void Dispose(bool disposing)
        {
            if (!disposed)
            {
                if (disposing)
                {
                    context.Dispose();
                }
            }
            this.disposed = true;
        }
        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }

        public void Save()
        {
            this.context.SaveChanges();
        }
    }
}
