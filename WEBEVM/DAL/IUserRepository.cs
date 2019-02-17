using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using Model;

namespace DAL
{
    public interface IUserRepository
    {
        void Insert(User entity);
        void Delete(object id);
        void Delete(User entityToDelete);
        void Update(User entityToUpdate);
        User GetById(object Id);

        IEnumerable<User> Get(Expression<Func<User, bool>> filter = null,
            Func<IQueryable<User>, IOrderedQueryable<User>> orderby = null);

        int GetCount(Expression<Func<User, bool>> filter = null);

        IEnumerable<User> Get(out int total, out int totalDisplay,
            Expression<Func<User, bool>> filter = null,
            Func<IQueryable<User>, IOrderedQueryable<User>> orderby = null,
            int pageIndex = 1, int pageSize = 10);
    }
}