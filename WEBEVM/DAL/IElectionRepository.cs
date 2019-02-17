using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using Model;

namespace DAL
{
    public interface IElectionRepository
    {
        void Insert(Election entity);
        void Delete(object id);
        void Delete(Election entityToDelete);
        void Update(Election entityToUpdate);
        Election GetById(object Id);

        IEnumerable<Election> Get(Expression<Func<Election, bool>> filter = null,
            Func<IQueryable<Election>, IOrderedQueryable<Election>> orderby = null);

        int GetCount(Expression<Func<Election, bool>> filter = null);

        IEnumerable<Election> Get(out int total, out int totalDisplay,
            Expression<Func<Election, bool>> filter = null,
            Func<IQueryable<Election>, IOrderedQueryable<Election>> orderby = null,
            int pageIndex = 1, int pageSize = 10);
    }
}